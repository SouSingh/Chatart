import streamlit as st
import json

class ArtistPortfolioApp:
    def __init__(self):
        st.title("Artist Portfolio")


        # Artist Information
        self.artist_name = st.text_input("Artist Name", placeholder="Your Name")
        self.description = st.text_area("Description", placeholder="Brief description of yourself and your artistic focus")
        self.website_url = st.text_input("Artist Website", placeholder="https://yourname.example.com")
        self.biography = st.text_area("Artist Biography", placeholder="A comprehensive biography detailing your art journey, education, and notable achievements, milestones, exhibitions, and projects")
        self.statement = st.text_area("Artist Statement", placeholder="A statement outlining your artistic philosophy, intent, interests, and vision, creative process, inspiration, and conceptual approach to your work. Incorporate elements that hold personal meaning for you, e.g. from nature.")
        self.media_list = st.text_area("Artist Media", placeholder="List of your favorite magazines, blogs, profiles, forums, pages, streams, YouTube channels, or exhibitions that have influenced your work, e.g. [Blog](https://www.blog.com/), Etc.")
        self.interests = st.text_area("Artist Interests", placeholder="List any interests or passions that may influence or inform your artistic work, especially in the fields of design, architecture, music, fashion, etc., e.g. metabolism, jazz, sustainable fashion")
        self.artistic_process = st.text_area("Artistic Process", placeholder="Outline your creative process, from initial idea to finished artwork, explaining the steps, decisions, and challenges you encountered along the way")
        self.personal_significance = st.text_area("Personal Significance", placeholder="Share any personal connections or meanings that your work holds for you as the artist")
        self.reviews = st.text_area("Reviews and Critical Reception", placeholder="Include notable reviews, critiques, or analysis of your artwork from art critics, journalists, or scholars, and any positive or negative feedback that you have received or that you can remember")
        self.contact_info = st.text_area("Artist Contact Information", placeholder="Your preferred contact details, like email address, phone number, or social media handles")
        self.references = st.text_area("References or External Links", placeholder="Relevant publications, interviews, articles, or resources where your work has been featured, e.g. [Article Title](https://example.com/article-url)")

    def validate_data(self):
        required_fields = [
            self.artist_name,
            self.description,
            self.website_url,
            self.biography,
            self.statement,
            self.media_list,
            self.interests,
            self.artistic_process,
            self.personal_significance,
            self.reviews,
            self.contact_info,
            self.references,
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Your") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save all artist data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/artist_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Check if the artist's name is already in the existing data
            existing_names = [entry.get("artist_name", "") for entry in existing_data]
            if self.artist_name in existing_names:
                st.warning("Artist with this name already exists. Please update the existing entry.")
                return

            # Append new data
            data_to_save = {
                "artist_name": self.artist_name,
                "description": self.description,
                "website_url": self.website_url,
                "biography": self.biography,
                "statement": self.statement,
                "media_list": self.media_list,
                "interests": self.interests,
                "artistic_process": self.artistic_process,
                "personal_significance": self.personal_significance,
                "reviews": self.reviews,
                "contact_info": self.contact_info,
                "references": self.references,
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/artist_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON"):
            self.save_data_to_json()

class ArtworkPortfolioApp:
    def __init__(self):
        st.title("Artwork Portfolio")



        # Artwork Information
        self.artwork_title = st.text_input("Artwork Title", key="artwork_title", placeholder="Title of Your Artwork")
        self.date_created = st.text_input("Date Created", key="date_created", placeholder="Year of Creation")
        self.art_medium = st.text_input("Art Medium", key="art_medium", placeholder="Art Medium e.g., 'Oil on Canvas', 'Sculpture'")
        self.artform = st.text_input("Artform", key="artform", placeholder="Specific Artform or Technique e.g., 'Photography', 'Sculpture'")
        self.dimensions_width = st.text_input("Width (in cm, in, or virtual units)", key="dimensions_width", placeholder="Width")
        self.dimensions_height = st.text_input("Height (in cm, in, or virtual units)", key="dimensions_height", placeholder="Height")
        self.dimensions_depth = st.text_input("Depth (in cm, in, or 'N/A')", key="dimensions_depth", placeholder="Depth")
        self.description = st.text_area("Description of Artwork", key="description", placeholder="A brief visual description of your artwork from a naive perspective, including its details, concept, colors, unique features, techniques, subject matter, themes, goals, contextual elements etc.")
        self.art_movement = st.text_input("Art Movement", key="art_movement", placeholder="The art movement or style your work belongs to or is influenced by, e.g., 'Bio Art', 'Surrealism', 'Ai Art', 'Post Digital Art', 'Mixed Media', 'Immersive Art', 'Land Art'")
        self.inspirations = st.text_area("Inspirations", key="inspirations", placeholder="List music, artists, works, events, or other sources of inspiration that you like or that influenced your artwork")
        self.artistic_techniques = st.text_area("Artistic Techniques", key="artistic_techniques", placeholder="Describe key techniques, materials, tools, or processes used in the creation of your artwork")
        self.materials = st.text_area("Materials", key="materials", placeholder="List the materials used in the creation of your artwork, such as paint, clay, wood, metal, etc.")
        self.subject_matter = st.text_area("Subject Matter", key="subject_matter", placeholder="Briefly describe the subject matter of your artwork and its significance within the context of your artistic practice")
        self.contextual_elements = st.text_area("Contextual Elements", key="contextual_elements", placeholder="Describe any objects, themes, images, networks, historical, cultural, social, or political context that informed or influenced your artwork")
        self.motifs = st.text_area("Motifs", key="motifs", placeholder="List any recurring motifs and metaphors or patterns present in your artistic process and explain their meaning or significance")
        # Add more fields as needed

    def validate_data(self):
        required_fields = [
            self.artwork_title,
            self.date_created,
            self.art_medium,
            self.artform,
            self.dimensions_width,
            self.dimensions_height,
            self.dimensions_depth,
            self.description,
            self.art_movement,
            self.inspirations,
            self.artistic_techniques,
            self.materials,
            self.subject_matter,
            self.contextual_elements,
            self.motifs,
            # Add more fields as needed
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Your") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save artwork data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/artwork_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "artwork_title": self.artwork_title,
                "date_created": self.date_created,
                "art_medium": self.art_medium,
                "artform": self.artform,
                "dimensions_width": self.dimensions_width,
                "dimensions_height": self.dimensions_height,
                "dimensions_depth": self.dimensions_depth,
                "description": self.description,
                "art_movement": self.art_movement,
                "inspirations": self.inspirations,
                "artistic_techniques": self.artistic_techniques,
                "materials": self.materials,
                "subject_matter": self.subject_matter,
                "contextual_elements": self.contextual_elements,
                "motifs": self.motifs,
                # Add more fields as needed
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/artwork_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="save_button"):
            self.save_data_to_json()

class SalesPricingApp:
    def __init__(self):
        st.title("Sales and Pricing Information")



        # Sales and Pricing Information
        self.asking_price = st.text_input("Asking Price", key="asking_price", placeholder="Artwork's asking price, in your preferred currency")
        self.payment_options = st.text_area("Payment Options", key="payment_options", placeholder="List accepted payment methods such as credit card, PayPal, cryptocurrency, etc.")
        self.discounts_offers = st.text_area("Discounts or Offers", key="discounts_offers", placeholder="Include details about any discounts, bundle offers, or other promotions related to your artwork")
        self.shipping_information = st.text_area("Shipping Information", key="shipping_information", placeholder="Specify shipping options, insurance, cost, estimated delivery time, handling fees, etc.")
        self.returns_policy = st.text_area("Returns Policy", key="returns_policy", placeholder="Provide details about your return policy, including timeframes, conditions for accepting returns, and refund process")
        self.limited_editions = st.text_area("Limited Editions", key="limited_editions", placeholder="If your artwork is part of a limited edition series, specify the edition size, numbering, and any special features, such as signed certificates of authenticity")
        self.purchase_information = st.text_area("Purchase Information", key="purchase_information", placeholder="Provide details on how interested parties can purchase or inquire about your artwork, including contact information, pricing, and any available editions")
        self.authentication = st.text_area("Authentication", key="authentication", placeholder="Describe the process for ensuring the authenticity of your artwork, such as hand-signed certificates, holographic seals, or online verification systems")
        self.availability = st.text_area("Availability", key="availability", placeholder="State the current availability of your artwork, whether it's in stock, on backorder, or sold out")
        self.licensing_options = st.text_area("Licensing Options", key="licensing_options", placeholder="If you offer licensing options for your artwork, include a brief description and pricing information for available licenses")
        self.inquiries = st.text_area("Inquiries", key="inquiries", placeholder="Provide contact information for sales inquiries, such as an email address, contact form, or phone number")
        # Add more fields as needed

    def validate_data(self):
        required_fields = [
            self.asking_price,
            self.payment_options,
            self.discounts_offers,
            self.shipping_information,
            self.returns_policy,
            self.limited_editions,
            self.purchase_information,
            self.authentication,
            self.availability,
            self.licensing_options,
            self.inquiries,
            # Add more fields as needed
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Artwork's") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save sales and pricing data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/sales_pricing_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "asking_price": self.asking_price,
                "payment_options": self.payment_options,
                "discounts_offers": self.discounts_offers,
                "shipping_information": self.shipping_information,
                "returns_policy": self.returns_policy,
                "limited_editions": self.limited_editions,
                "purchase_information": self.purchase_information,
                "authentication": self.authentication,
                "availability": self.availability,
                "licensing_options": self.licensing_options,
                "inquiries": self.inquiries,
                # Add more fields as needed
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/sales_pricing_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="sales_save_button"):
            self.save_data_to_json()

class ExhibitionsProjectsApp:
    def __init__(self):
        st.title("Exhibitions and Projects")

        # Example Part
        st.markdown("### Example:")
        st.markdown("Replace the placeholder text with your actual information.")

        # Exhibitions and Projects Information
        self.exhibition_dates = st.text_area("Exhibition Dates", key="exhibition_dates", placeholder="List details of any upcoming exhibitions or events featuring your artwork")
        # Add more fields as needed

    def validate_data(self):
        required_fields = [
            self.exhibition_dates,
            # Add more fields as needed
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("List details") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save exhibitions and projects data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/exhibitions_projects_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "exhibition_dates": self.exhibition_dates,
                # Add more fields as needed
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/exhibitions_projects_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="exb_save_button"):
            self.save_data_to_json()


class WorkPresentationApp:
    def __init__(self):
        st.title("Work Presentation")

        # Example Part

        # Work Presentation Information
        self.editions_variants = st.text_area("Editions and Variants", key="editions_variants", placeholder="Details of any different editions, variants, or versions of your artwork and how they differ from the original")
        self.installation_instructions = st.text_area("Installation Instructions", key="installation_instructions", placeholder="Provide instructions on how to properly install, display, or interact with your artwork, if applicable")
        self.maintenance_preservation = st.text_area("Maintenance and Preservation", key="maintenance_preservation", placeholder="Recommendations for maintaining and preserving your artwork, including proper handling, storage, and cleaning procedures")
        self.edition_details = st.text_area("Edition Details", key="edition_details", placeholder="For editioned works, provide information on edition size, numbering, availability, and pricing")
        self.availability_pricing = st.text_area("Availability and Pricing", key="availability_pricing", placeholder="Provide information on the availability and pricing of your artwork, including any information on discounts, promotions, or special offers")

        # Additional Supporting Materials
        st.markdown("### Additional Supporting Materials:")
        self.images = st.text_area("Images", key="images", placeholder="Provide high-resolution images or specifications for the artwork, including detailed shots or images showing the artwork in different contexts")
        self.video = st.text_input("Video", key="video", placeholder="If applicable, provide a link to a video showcasing the artwork and/or the process of creating it")
        self.audio = st.text_input("Audio", key="audio", placeholder="If applicable, provide a link to an audio component that is part of or complements the artwork")
        self.additional_materials = st.text_area("Additional Materials", key="additional_materials", placeholder="Provide links to supporting materials, such as video or audio documentation, digital versions of your artwork, critical reviews, or related research")
        self.accessibility_info = st.text_area("Accessibility Info", key="accessibility_info", placeholder="Provide any relevant accessibility information, such as image alt text, video/audio transcripts, or ways viewers with disabilities can engage with your artwork")
        # Add more fields as needed

    def validate_data(self):
        required_fields = [
            self.editions_variants,
            self.installation_instructions,
            self.maintenance_preservation,
            self.edition_details,
            self.availability_pricing,
            self.images,
            self.video,
            self.audio,
            self.additional_materials,
            self.accessibility_info,
            # Add more fields as needed
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Details") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save work presentation and supporting materials data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/work_presentation_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "editions_variants": self.editions_variants,
                "installation_instructions": self.installation_instructions,
                "maintenance_preservation": self.maintenance_preservation,
                "edition_details": self.edition_details,
                "availability_pricing": self.availability_pricing,
                "images": self.images,
                "video": self.video,
                "audio": self.audio,
                "additional_materials": self.additional_materials,
                "accessibility_info": self.accessibility_info,
                # Add more fields as needed
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/work_presentation_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="work_save_button"):
            self.save_data_to_json()

class ArtCriteriaApp:
    def __init__(self):
        st.title("Art Criteria and Parameters")

        # Example Part


        # Art Criteria and Parameters
        self.aesthetic_quality = st.text_area("Aesthetic Quality", key="aesthetic_quality", placeholder="Statement about the aesthetic quality of your artwork")
        self.conceptual_relevance = st.text_area("Conceptual Relevance", key="conceptual_relevance", placeholder="Statement about the conceptual relevance of your artwork")
        self.technological_innovation = st.text_area("Technological Innovation", key="technological_innovation", placeholder="Statement about the technological innovation of your artwork")
        self.interdisciplinary_approach = st.text_area("Interdisciplinary Approach", key="interdisciplinary_approach", placeholder="Statement about the interdisciplinary approach of your artwork")
        self.audience_interaction = st.text_area("Audience Interaction", key="audience_interactio", placeholder="Statement about the audience interaction with your artwork")
        self.interactive_elements = st.text_area("Interactive Elements", key="interactive_elements", placeholder="If applicable, describe any interactive features or components in the artwork")
        self.accessibility = st.text_area("Accessibility", key="accessibility", placeholder="Explain how you have considered accessibility in your artwork")
        self.critical_reception = st.text_area("Critical Reception", key="critical_reception", placeholder="Describe how you feel about any critical response your artwork has received")
        self.contextual_analysis = st.text_area("Contextual Analysis", key="contextual_analysis", placeholder="Provide an analysis of your artwork within the context of your artistic practice")
        self.challenges_overcome = st.text_area("Challenges Overcome", key="challenges_overcome", placeholder="Discuss any challenges or obstacles you faced during the creation of your artwork")
        self.personal_significance = st.text_area("Personal Significance", key="personal_significance", placeholder="Share any personal or emotional significance your artwork holds for you")
        self.future_plans = st.text_area("Future Plans", key="future_plans", placeholder="Outline any plans or ambitions you have for the future of this artwork")

    def validate_data(self):
        required_fields = [
            self.aesthetic_quality,
            self.conceptual_relevance,
            self.technological_innovation,
            self.interdisciplinary_approach,
            self.audience_interaction,
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("Statement about") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save art criteria and parameters data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/art_criteria_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "aesthetic_quality": self.aesthetic_quality,
                "conceptual_relevance": self.conceptual_relevance,
                "technological_innovation": self.technological_innovation,
                "interdisciplinary_approach": self.interdisciplinary_approach,
                "audience_interaction": self.audience_interaction,
                "interactive_elements": self.interactive_elements,
                "accessibility": self.accessibility,
                "critical_reception": self.critical_reception,
                "contextual_analysis": self.contextual_analysis,
                "challenges_overcome": self.challenges_overcome,
                "personal_significance": self.personal_significance,
                "future_plans": self.future_plans,
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/art_criteria_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="art_save_button"):
            self.save_data_to_json()


class ArtisticQuestionsApp:
    def __init__(self):
        st.title("Artistic Questions")


        # Artistic Questions
        self.art_historical_context = st.text_area("Art Historical Context", key="art_historical_contet", placeholder="Does your work engage with or contribute to the greater art historical context?")
        self.cultural_historical_societal_influences = st.text_area("Cultural, Historical, and Societal Influences", key="cultural_historical_societal_influences", placeholder="Are there specific cultural, historical, or societal influences that have shaped your art practice?")
        self.theory_and_philosophy = st.text_area("Theory and Philosophy", key="theory_and_philosophy", placeholder="What theories or philosophies inform your artistic practice and artwork?")
        self.artistic_practice_evolution = st.text_area("Artistic Practice Evolution", key="artistic_practice_evolution", placeholder="How does your artistic practice evolve or change over time? Is there a specific trajectory that you can trace?")
        self.techniques_materials_processes = st.text_area("Techniques, Materials, and Processes", key="techniques_materials_processes", placeholder="What specific techniques, materials, or processes have you employed in your work, and how do these choices contribute to its overall meaning or effect?")
        self.audience_interaction = st.text_area("Audience Interaction", key="audience_interaction", placeholder="In what ways does your artwork invite audience interaction, and how critical is this interaction to the overall experience or interpretation of the piece?")
        self.influences_and_inspirations = st.text_area("Influences and Inspirations", key="influences_and_inspirations", placeholder="Can you provide any examples of other artists or artworks that have influenced your practice or approach to your work?")
        self.current_art_landscape = st.text_area("Current Art Landscape", key="current_art_landscape", placeholder="How do you see your artwork fitting within the current art landscape or engaging in larger art-related conversations?")
        self.challenges_and_obstacles = st.text_area("Challenges and Obstacles", key="challenges_and_obstacles", placeholder="Are there any challenges or obstacles you faced while creating this artwork, and how did these experiences shape the final piece?")
        self.message_and_intention = st.text_area("Message and Intention", key="message_and_intention", placeholder="Is there a message or intention behind your artwork that you hope to communicate to your audience, and how do you hope they engage with it?")
        self.interdisciplinary_approaches = st.text_area("Interdisciplinary Approaches", key="interdisciplinary_approaches", placeholder="Does your artwork incorporate any interdisciplinary approaches, such as collaborations with professionals from different fields, research in various disciplines, or the application of knowledge from multiple sources?")
        self.future_projects_and_collaborations = st.text_area("Future Projects and Collaborations", key="future_projects_and_collaborations", placeholder="Are there any upcoming projects, exhibitions, or collaborations that you are currently working on or plan to work on in the future? If so, how do these endeavors connect to your existing body of work?")
        self.artwork_understanding = st.text_area("Artwork Understanding", key="artwork_understanding", placeholder="How has your understanding of your artwork shifted or evolved throughout the creation process, and what insights have you gained as a result?")
        self.provoking_conversation = st.text_area("Provoking Conversation", key="provoking_conversation", placeholder="In what ways do you hope your artwork provokes conversation, sparks debate, or inspires thought among your audience?")
        self.artistic_practice_future = st.text_area("Artistic Practice Future", key="artistic_practice_future", placeholder="How do you envision the future of your artistic practice, and what areas or themes do you hope to explore moving forward?")
        self.community_and_network_support = st.text_area("Community and Network Support", key="community_and_network_support", placeholder="Are there any communities, organizations, or networks that have supported you or your work, and how have these connections impacted your artistic practice and experiences?")

    def validate_data(self):
        required_fields = [
            self.art_historical_context,
            self.cultural_historical_societal_influences,
            self.theory_and_philosophy,
            self.artistic_practice_evolution,
            self.techniques_materials_processes,
            self.audience_interaction,
            self.influences_and_inspirations,
            self.current_art_landscape,
            self.challenges_and_obstacles,
            self.message_and_intention,
            self.interdisciplinary_approaches,
            self.future_projects_and_collaborations,
            self.artwork_understanding,
            self.provoking_conversation,
            self.artistic_practice_future,
            self.community_and_network_support,
        ]

        # Check if any required field is blank
        if any(not field or field.startswith("What") for field in required_fields):
            st.warning("Please fill in all the required fields.")
            return False
        return True

    def save_data_to_json(self):
        """
        Save artistic questions data to a JSON file.
        """
        try:
            # Validate data before saving
            if not self.validate_data():
                return

            # Load existing data if the file exists
            try:
                with open("data/Artist/artistic_questions_data.json", "r") as existing_file:
                    existing_data = json.load(existing_file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = []

            # Append new data
            data_to_save = {
                "art_historical_context": self.art_historical_context,
                "cultural_historical_societal_influences": self.cultural_historical_societal_influences,
                "theory_and_philosophy": self.theory_and_philosophy,
                "artistic_practice_evolution": self.artistic_practice_evolution,
                "techniques_materials_processes": self.techniques_materials_processes,
                "audience_interaction": self.audience_interaction,
                "influences_and_inspirations": self.influences_and_inspirations,
                "current_art_landscape": self.current_art_landscape,
                "challenges_and_obstacles": self.challenges_and_obstacles,
                "message_and_intention": self.message_and_intention,
                "interdisciplinary_approaches": self.interdisciplinary_approaches,
                "future_projects_and_collaborations": self.future_projects_and_collaborations,
                "artwork_understanding": self.artwork_understanding,
                "provoking_conversation": self.provoking_conversation,
                "artistic_practice_future": self.artistic_practice_future,
                "community_and_network_support": self.community_and_network_support,
            }

            existing_data.append(data_to_save)

            # Save the updated data to the file
            with open("data/Artist/artistic_questions_data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            st.success("Data saved to JSON successfully!")
        except Exception as e:
            st.error(f"Error saving data to JSON: {e}")

    def run(self):
        # Save to JSON Button
        if st.button("Save to JSON", key="quest_save_button"):
            self.save_data_to_json()



def overall():
    artist_app = ArtistPortfolioApp()
    artist_app.run()
    artwork_app = ArtworkPortfolioApp()
    artwork_app.run()
    sales_pricing_app = SalesPricingApp()
    sales_pricing_app.run()
    exhibitions_projects_app = ExhibitionsProjectsApp()
    exhibitions_projects_app.run()
    work_presentation_app = WorkPresentationApp()
    work_presentation_app.run()
    art_criteria_app = ArtCriteriaApp()
    art_criteria_app.run()
    artistic_questions_app = ArtisticQuestionsApp()
    artistic_questions_app.run()




