import streamlit as st
import json

class CopyrightLicensingApp:
    def __init__(self):
        st.title("Copyright and Licensing Information")

        # Example Part
        st.markdown("### Example:")
        st.markdown("Replace the placeholder text with your actual information.")

        # Copyright and Licensing Information
        self.copyright = st.text_area("Copyright", key="copyright", placeholder="Indicate the copyright holder(s) and any relevant information regarding copyright ownership, e.g., '© 2021 Your Name. All rights reserved.'")
        self.licensing = st.text_area("Licensing", key="licensing", placeholder="Specify any terms and conditions regarding how the artwork can be used, reproduced, or distributed, e.g., 'This artwork is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. Link: [http://creativecommons.org/licenses/by-nc-nd/4.0/]'")
        self.usage_permissions = st.text_area("Usage Permissions", key="usage_permissions", placeholder="Clearly state permissions and restrictions on how the artwork may be used or shared, including permission for educational, commercial, or public display purposes")

        # Checkboxes
        self.include_contact_info = st.checkbox("Include Contact Information")
        self.include_social_media = st.checkbox("Include Social Media")
        self.include_image_credits = st.checkbox("Include Image Credits")

        # Conditional Display based on checkboxes
        if self.include_contact_info:
            self.contact_information = st.text_area("Contact Information", key="contact_information", placeholder="Provide contact information for Inquiries: `<Provide an email address or other method for viewers, collectors, or institutions to contact you with any questions, requests, or inquiries about the artwork, e.g., 'Please direct all inquiries to [email@example.com](mailto:email@example.com)>'")

        if self.include_social_media:
            self.social_media = st.text_area("Social Media", key="social_media", placeholder="List any social media platforms where your artwork is showcased or where followers can stay updated on your work, e.g., 'Follow me on Instagram: [https://www.instagram.com/yourusername](https://www.instagram.com/yourusername)'")

        if self.include_image_credits:
            self.image_credits = st.text_area("Image Credits", key="image_credits", placeholder="Provide appropriate image credits for photos, videos, or other media used within your artwork or metadata, including the name of the photographer or creator and a link to their webpage if applicable")

    def validate_data(self):
        required_fields = [
            self.copyright,
            self.licensing,
            self.usage_permissions,
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Indicate") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save copyright and licensing data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("copyright_licensing_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "copyright": self.copyright,
                "licensing": self.licensing,
                "usage_permissions": self.usage_permissions,
            }

            if self.include_contact_info:
                data_to_save["contact_information"] = self.contact_information

            if self.include_social_media:
                data_to_save["social_media"] = self.social_media

            if self.include_image_credits:
                data_to_save["image_credits"] = self.image_credits

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("copyright_licensing_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="save_button"):
            self.save_data_to_json()

if __name__ == "__main__":
    copyright_licensing_app = CopyrightLicensingApp()
    copyright_licensing_app.run()
