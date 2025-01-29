from __future__ import unicode_literals

import frappe
from erpnext import get_company_currency
from erpnext.accounts.party import get_party_account, get_party_account_currency
from erpnext.accounts.utils import get_account_currency
from frappe.utils import cint


def on_submit(doc, event):
    if cint(
        frappe.get_value(
            "LCV Addons Settings", "LCV Addons Settings", "enable_auto_expense_on_lcv"
        )
    ):
        validate(doc)
        make_expense_je(doc)


def on_cancel(doc, event):
    if cint(
        frappe.get_value(
            "LCV Addons Settings", "LCV Addons Settings", "enable_auto_expense_on_lcv"
        )
    ):
        cancel_expense_je(doc)


def validate(doc):
    validate_currency(doc)
    validate_no_paid_supplier(doc)


def validate_currency(doc):
    for expense in doc.taxes:
        if expense.party and expense.party_type:
            party_account_currency = get_party_account_currency(
                expense.party_type, expense.party, doc.company
            )
            if not party_account_currency == get_company_currency(doc.company):
                frappe.throw(
                    "Currency Conversion is not supported when creating Journal entry from LCV."
                )

        if expense.is_paid or expense.paid_from_account:
            if not get_account_currency(
                expense.paid_from_account
            ) == get_company_currency(doc.company):
                frappe.throw(
                    "Currency Conversion is not supported when creating Journal entry from LCV."
                )


def validate_no_paid_supplier(doc):
    for expense in doc.taxes:
        if expense.is_paid:
            if expense.party or expense.party_type:
                frappe.throw("You cannot set party or party type for a paid Expense.")


def make_expense_je(doc):
    journal_entry = frappe.new_doc("Journal Entry")
    journal_entry.company = doc.company
    journal_entry.posting_date = doc.posting_date

    for expense in doc.taxes:
        if expense.is_paid and expense.paid_from_account and expense.expense_account:
            debit_entry = {
                "account": expense.expense_account,
                "debit": expense.amount,
                "debit_in_account_currency": expense.amount,
            }
            journal_entry.append("accounts", debit_entry)

            credit_entry = {
                "account": expense.paid_from_account,
                "credit": expense.amount,
                "credit_in_account_currency": expense.amount,
            }
            journal_entry.append("accounts", credit_entry)

        elif expense.party and expense.party_type and expense.expense_account:
            party_account = get_party_account(
                expense.party_type, expense.party, doc.company
            )

            debit_entry = {
                "account": expense.expense_account,
                "debit": expense.amount,
                "debit_in_account_currency": expense.amount,
            }
            journal_entry.append("accounts", debit_entry)

            credit_entry = {
                "party_type": expense.party_type,
                "party": expense.party,
                "account": party_account,
                "credit": expense.amount,
                "credit_in_account_currency": expense.amount,
            }
            journal_entry.append("accounts", credit_entry)

    if getattr(journal_entry, "accounts", False):
        journal_entry.save()
        journal_entry.submit()
        doc.db_set("journal_entry", journal_entry.name)


def cancel_expense_je(doc):
    if doc.journal_entry:
        je = frappe.get_doc("Journal Entry", doc.journal_entry)
        je.cancel()


def sum_invoice_and_charges(doc, event):
    doc.sum_invoice_and_charges = sum(
        [item.get("amount") + item.get("applicable_charges") for item in doc.items]
    )


def sum_invoice_and_charges_patch():
    landed_cost_vouchers = frappe.db.get_list(
        "Landed Cost Voucher", pluck="name", filters={"docstatus": 1}
    )
    for docname in landed_cost_vouchers:
        landed_cost = frappe.get_doc("Landed Cost Voucher", docname)
        if landed_cost.sum_invoice_and_charges:
            continue
        sum_invoice_and_charges = sum(
            [
                item.get("amount") + item.get("applicable_charges")
                for item in landed_cost.items
            ]
        )
        value_before_update = landed_cost.sum_invoice_and_charges
        landed_cost.db_set("sum_invoice_and_charges", sum_invoice_and_charges, commit=1)
        print(
            f"\n{landed_cost.name} sum_invoice_and_charges is updated from {value_before_update} to {landed_cost.sum_invoice_and_charges}."
        )
