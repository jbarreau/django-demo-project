from django_forest.utils.collection import Collection

from library.models import Users

class UserForest(Collection):
    def load(self):
        self.fields = [{
            "field": "creditCard",
            "type": "String",
            "get": self.get_credit_card,
        }]

    def get_credit_card(self, obj):
        return f"""<div class="card-wrapper">
                    <div class="card-container"
                        style="font-size: 14px; border-radius: 10px; width: 250px; height: 140px; background-color: #444857; color: white; padding: 10px">
                        <div class="card-number-container" style="margin-top: 5px">
                            <div class="card-info-title" style="color: #9399af; ">card number</div>
                            <div class="card-info-value" style="font-size: 12px">' {obj.name} '</div>
                        </div>
                        <div class="card-name-date-container" style="display: flex; margin-top: 20px">
                            <div class="card-name-container">
                                <div class="card-info-title" style="color: #9399af; ">card holder</div>
                                <div class="card-info-value" style="font-size: 12px">' {obj.name} '</div>
                            </div>
                            <div class="card-date-container" style="margin: auto">
                                <div class="card-info-title" style="color: #9399af; ">expires at</div>
                                <div class="card-info-value" style="font-size: 12px">' {obj.created_at} '</div>
                            </div>
                        </div>
                    </div>
                </div>"""


Collection.register(UserForest, Users)