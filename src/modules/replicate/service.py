import os
import replicate

os.environ.get("REPLICATE_API_TOKEN")

class ReplicateService:
    def generate_alt_text(self, imageUrl: str) -> str:
        # Run ML Model with imageUrl
        model = replicate.models.get("salesforce/blip")
        version = model.versions.get("2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746")

        # Get the alt text result and return it
        return version.predict(image=imageUrl)