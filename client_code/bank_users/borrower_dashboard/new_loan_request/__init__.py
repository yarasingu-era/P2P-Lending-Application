from ._anvil_designer import new_loan_requestTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import borrower_main_form_module as main_form_module

class new_loan_request(new_loan_requestTemplate):
    def __init__(self, **properties):
        self.user_id = main_form_module.userId
        self.init_components(**properties)
        # self.max_amount_lb.text = f"200000
        # self.name.selected_value=app_tables.product_group.search()
        
        options = app_tables.product_group.search()
        option_strings = [option['name'] for option in options]
        self.name.items = option_strings
        self.name.selected_value = option_strings[0] if option_strings else None 

    def name_change(self, **event_args):
        selected_value = self.name.selected_value

        if selected_value:
          self.label_1.visible = True
          self.label_2.visible = True
          self.name.visible = True
          self.drop_down_2.visible = True

            # Fetch product categories based on the selected loan type
          product_categories = app_tables.product_categories.search(
          name_group=selected_value
          )

          if product_categories:
            # Display product categories in drop_down_2
            self.drop_down_2.items = [category['name_categories'] for category in product_categories]
            self.drop_down_2.selected_value = product_categories[0]['name_categories'] if product_categories else None
 

    def button_1_click(self, **event_args):
        open_form('bank_users.borrower_dashboard')

    def button_1_copy_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('bank_users.borrower_dashboard.new_loan_request.loan_type')

    def max_amount_lb_show(self, **event_args):
      """This method is called when the Label is shown on the screen"""
              
        options = app_tables.product_detai
        option_strings = [option['max_amount'] for option in options]
        self.name.items = option_strings
        self.name.selected_value = option_strings[0] if option_strings else None 

