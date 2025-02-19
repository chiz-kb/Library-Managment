# Copyright (c) 2025, Gemechis Kebenessa and contributors
# For license information, please see license.txt

# import frappe
from frappe import frappe
from frappe.model.document import Document


class Loan(Document):
 def before_submit(self):
  active_loan = frappe.db.exists("Loan",{"member": self.member,"return_date": (">", self.return_date),},)
  if active_loan:
   frappe.throw("This member already has an active loan and cannot take another loan at this time.")
  book_taken = frappe.db.exists("Loan",{"member": self.member,"return_date": (">", self.return_date),},)
  if book_taken:
   frappe.throw("This book is already loaned out and cannot be borrowed at this time")