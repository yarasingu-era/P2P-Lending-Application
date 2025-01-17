from ._anvil_designer import add_product_categories_and_groupsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_product_categories_and_groups(add_product_categories_and_groupsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    options = app_tables.product_group.search()
    option_strings = [option['name'] for option in options]
    self.drop_down_1.items = option_strings
    self.drop_down_1.selected_value = option_strings[0] if option_strings else None   

  # def name_change(self, **event_args):
  #       self.selected_value = self.drop_down_1.selected_value

  #       if self.selected_value:
  #         self.label_1.visible = True
  #         self.label_2.visible = True
  #         self.drop_down_1.visible = True
  #         self.text_box_1.visible = True


  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Get selected values
        selected_group = self.drop_down_1.selected_value
        text_box_value = self.text_box_1.text

        # Check if both values are selected or entered
        if selected_group and text_box_value:
            # Create a new row in the product_categories table and set the values
            app_tables.product_categories.add_row(
                name_group=selected_group,
                name_categories=text_box_value
            )
            # Optionally, you can show a confirmation message
            alert("Product category saved successfully!")
            # Clear the input fields after saving
            self.drop_down_1.selected_value = None
            self.text_box_1.text = ""
            open_form('admin.dashboard.manage_products')
        else:
            # Show an error message if one or both values are not selected or entered
            alert("Please enter/select all details before saving.")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('admin.dashboard.manage_products')
