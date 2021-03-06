from datetime import datetime

from formskit.validators import NotEmpty

from wewallet.application.forms import PostForm


class CreateBillForm(PostForm):

    def __init__(self, request, billing):
        super().__init__(request)
        self.billing = billing

    def create_form(self):
        self.add_field('place', label='Miejsce', validators=[NotEmpty()])

    def on_success(self):
        data = self.get_data_dict(True)
        self.drivers.bill.create(
            billing_id=self.billing.id,
            place=data['place'],
            date=datetime.utcnow(),
        )
        self.database().commit()
