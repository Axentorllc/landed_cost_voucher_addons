console.log("LCV loaded from landed cost voucher addons");
var LCV_ADDONS_SETTINGS = LCV_ADDONS_SETTINGS || {};

frappe.ui.form.on("Landed Cost Voucher", "refresh", function (frm) {
  frappe.call({
    method: "frappe.client.get",
    args: {
      doctype: "LCV Addons Settings",
      name: "LCV Addons Settings",
    },
    callback(r) {
      if (r.message) {
        LCV_ADDONS_SETTINGS = r.message;
        if (LCV_ADDONS_SETTINGS.enable_auto_expense_on_lcv) {
          frappe.ui.form.on("Landed Cost Voucher", {
            validate(frm) {
              let sum = 0.0;
              $.each(frm.doc.purchase_receipts, function (i, d) {
                sum += d.grand_total;
              });
              $.each(frm.doc.items, function (i, d) {
                d.item_total = d.amount + d.applicable_charges;
              });
              refresh_field("purchase_receipts");
              sum += frm.doc.total_taxes_and_charges;
              frm.doc.sum_invoice_and_charges = sum;
              refresh_field("sum_invoice_and_charges");
            },
          });

          frappe.ui.form.on("Landed Cost Voucher", "onload", function (frm) {
            frm.fields_dict["taxes"].grid.get_field("party_type").get_query =
              function (doc, cdt, cdn) {
                const row = locals[cdt][cdn];
                return {
                  filters: [["DocType", "name", "=", "Supplier"]],
                };
              };

            frm.fields_dict["taxes"].grid.get_field(
              "paid_from_account"
            ).get_query = function (doc, cdt, cdn) {
              const row = locals[cdt][cdn];
              return {
                filters: [
                  ["Account", "Company", "=", doc.company],
                  ["Account", "account_type", "in", ["Cash", "Bank"]],
                ],
              };
            };
          });
        }
      }
    },
  });
});
