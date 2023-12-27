import streamlit as st
import json
import os

def art_writing_portfolio():
    st.title("Art Writing Portfolio")

    # Art Writing Information
    title = st.text_input("Art Writing Title", key="art_writing_title", placeholder="Art Writing Title")
    date_created = st.text_input("Date Created", key="date_created", placeholder="Year of Creation")
    art_writing_type = st.text_input("Type", key="art_writing_type", placeholder="Art Writing Type e.g., Research Paper, Article, MHD Thesis, BA Thesis, PHD Thesis")

    # Dimensions
    st.subheader("Dimensions")
    pages = st.number_input("Pages", min_value=1, step=1, value=1, key="pages")
    page_format = st.text_input("Format", key="page_format", placeholder="Page Format")
    file_size = st.text_input("File Size", key="file_size", placeholder="File Size and File Format")

    description = st.text_area("Description of Art Writing", key="description", placeholder="A brief description of your writing, including its structure, concept, unique features, techniques, subject matter, themes, goals, and contextual elements")
    relevance = st.text_area("Relevance of the Art Writing", key="relevance", placeholder="Explain the relevance of your art writing in the context of the art world or related fields and how it contributes to the understanding of the subject at hand")
    themes = st.text_area("Themes", key="themes", placeholder="List the main themes explored in your art writing, such as historical aspects, artistic movements, cultural influences, or artistic practices")
    keywords = st.text_area("Keywords", key="keywords", placeholder="Key terms or phrases relevant to your art writing, used for indexing and searchability purposes")
    abstract = st.text_area("Abstract", key="abstract", placeholder="A concise summary of your art writing, outlining its main points, objectives, and conclusions")
    artworks_or_artists = st.text_area("Art Works or Artists Discussed", key="artworks_or_artists", placeholder="List the artworks or artists discussed in your art writing, if applicable")
    citation_information = st.text_area("Citation Information", key="citation_information", placeholder="Provide the recommended citation for your art writing, including your name, the title, date, and any necessary publication information")

    # Supplementary Materials
    st.subheader("Supplementary Materials")
    supplementary_materials = st.text_area("Supplementary Materials", key="supplementary_materials", placeholder="List any supplementary materials related to your art writing, such as images, videos, or additional documents")

    # Image Credits
    st.subheader("Image Credits")
    image_credits = st.text_area("Image Credits", key="image_credits", placeholder="Provide credit and sources for any images used in your art writing, including a brief description of each image and any necessary copyrights or permissions")

    # Video Credits
    st.subheader("Video Credits")
    video_credits = st.text_area("Video Credits", key="video_credits", placeholder="Provide credit and sources for any videos used in your art writing, including a brief description of each video and any necessary copyrights or permissions")

    # Related Publications
    st.subheader("Related Publications")
    related_publications = st.text_area("Related Publications", key="related_publications", placeholder="List any publications closely related to your art writing, such as previous works by you or other authors that elaborate or expand upon the themes, concepts, or techniques discussed in your writing")

    # Recommended Readings
    st.subheader("Recommended Readings")
    recommended_readings = st.text_area("Recommended Readings", key="recommended_readings", placeholder="List any books, articles, or other references you recommend for further reading, including the title, author, and publication year for each source")

    # References
    st.subheader("References")
    references = st.text_area("References", key="references", placeholder="List all sources actually cited in your art writing, following a specific citation style. Ensure to give full details such as title, author, publication year, and page numbers")

    # External Links
    st.subheader("External Links")
    external_links = st.text_area("External Links", key="external_links", placeholder="Provide any external links that offer additional insights or perspectives related to your art writing. These can include online articles, videos, presentations, archival material, databases, etc.")

    # Journal or Magazine Details
    st.subheader("Journal or Magazine Details")
    journal_name = st.text_input("Journal/Magazine Name", key="journal_name", placeholder="Name of the Journal or Magazine in which your art writing is published")
    publisher = st.text_input("Publisher", key="publisher", placeholder="Name of the Journal/Magazine Publisher")
    volume_and_issue = st.text_input("Volume and Issue", key="volume_and_issue", placeholder="The volume and issue number of the journal or magazine, if applicable")
    page_range = st.text_input("Page Range", key="page_range", placeholder="Exact page range where your art writing starts and ends in the journal or magazine")
    issn_or_isbn = st.text_input("ISSN or ISBN", key="issn_or_isbn", placeholder="Unique identifier number for the journal or the book, if applicable")
    doi = st.text_input("DOI", key="doi", placeholder="Digital Object Identifier if your art writing has one")
    date_of_publication = st.text_input("Date of Publication", key="date_of_publication", placeholder="Exact date (day, month, year) of your art writing publication")

    # Art Writing Key Takeaways
    st.subheader("Art Writing Key Takeaways")
    key_takeaway_1 = st.text_area("Key Takeaway 1", key="key_takeaway_1", placeholder="Summarize the main takeaway or learning from your art writing")
    key_takeaway_2 = st.text_area("Key Takeaway 2", key="key_takeaway_2", placeholder="Another important point or conclusion that readers should be aware of")
    key_takeaway_3 = st.text_area("Key Takeaway 3", key="key_takeaway_3", placeholder="Additional finding or insight that supports the overall argument or idea of your writing")

    # Personal Influence
    st.subheader("Personal Influence")
    personal_influence = st.text_area("Describe how researching and writing about art have informed or shaped your own practice, and how the process has led you to new understandings or discoveries in your field. Discuss the changes or growth you've experienced, and the relationships or connections you've made through your work", key="personal_influence")

    # Personal Journey
    st.subheader("Personal Journey")
    personal_journey = st.text_area("Detail how you will integrate the insights gained from your art writing into future projects, methodology, and overall research/work perspective", key="personal_journey")

    # Academic Context: Review
    st.subheader("Academic Context: Review")
    reviewer_1_name = st.text_input("Reviewed by 1", key="reviewer_1_name", placeholder="Name1_Full Prefix Credentials, if applicable e.g. Dr., Prof.")
    reviewer_2_name = st.text_input("Reviewed by 2", key="reviewer_2_name", placeholder="Name2_Full Prefix Credentials, if applicable e.g. Dr., Prof.")

    # Review Summary
    st.subheader("Review Summary")
    review_summary = st.text_area("Brief summary of the comprehensive review. Include specific comments by reviewers, the strengths and weaknesses they highlighted, and their recommendations for improvements or further development", key="review_summary")

    # Conclusion
    st.subheader("Conclusion")
    overall_evaluation = st.text_area("Overall summary/Evaluation: Evaluate, in summary, the quality, impact, and relevance of your art writing. Discuss the effectiveness of the argument or concept presented, its influence on the study of art, and its potential for future related research or work", key="overall_evaluation")

    st.subheader("Art Writing")
    art_writing_upload = st.file_uploader("Upload Art Writing (PDF, Word, Text)", type=["pdf", "docx", "txt"])
    if art_writing_upload is not None:
        art_writing_content = art_writing_upload.read()
        st.success("Art Writing uploaded successfully!")

    # Save to JSON Button
    save_button_key = "save_button_" + str(hash((title, date_created, art_writing_type)))
    if st.button("Save to JSON", key=save_button_key):
        save_data_to_json(title, date_created, art_writing_type, pages, page_format, file_size, description, relevance, themes, keywords, abstract, artworks_or_artists, citation_information, supplementary_materials, image_credits, video_credits, related_publications, recommended_readings, references, external_links, journal_name, publisher, volume_and_issue, page_range, issn_or_isbn, doi, date_of_publication, key_takeaway_1, key_takeaway_2, key_takeaway_3, personal_influence, personal_journey, reviewer_1_name, reviewer_2_name, review_summary, overall_evaluation, art_writing_content)

def save_data_to_json(title, date_created, art_writing_type, pages, page_format, file_size, description, relevance, themes, keywords, abstract, artworks_or_artists, citation_information, supplementary_materials, image_credits, video_credits, related_publications, recommended_readings, references, external_links, journal_name, publisher, volume_and_issue, page_range, issn_or_isbn, doi, date_of_publication, key_takeaway_1, key_takeaway_2, key_takeaway_3, personal_influence, personal_journey, reviewer_1_name, reviewer_2_name, review_summary, overall_evaluation, art_writing_content):
    try:
        # Load existing data if the file exists
        try:
            with open("data/art_writing_data.json", "r") as existing_file:
                existing_data = json.load(existing_file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append new data
        data_to_save = {
            "title": title,
            "date_created": date_created,
            "art_writing_type": art_writing_type,
            "dimensions": {
                "pages": pages,
                "page_format": page_format,
                "file_size": file_size,
            },
            "description": description,
            "relevance": relevance,
            "themes": themes,
            "keywords": keywords,
            "abstract": abstract,
            "artworks_or_artists": artworks_or_artists,
            "citation_information": citation_information,
            "supplementary_materials": supplementary_materials,
            "image_credits": image_credits,
            "video_credits": video_credits,
            "related_publications": related_publications,
            "recommended_readings": recommended_readings,
            "references": references,
            "external_links": external_links,
            "journal_details": {
                "journal_name": journal_name,
                "publisher": publisher,
                "volume_and_issue": volume_and_issue,
                "page_range": page_range,
                "issn_or_isbn": issn_or_isbn,
                "doi": doi,
                "date_of_publication": date_of_publication,
            },
            "key_takeaways": {
                "1": key_takeaway_1,
                "2": key_takeaway_2,
                "3": key_takeaway_3,
            },
            "personal_influence": personal_influence,
            "personal_journey": personal_journey,
            "academic_review": {
                "reviewer_1_name": reviewer_1_name,
                "reviewer_2_name": reviewer_2_name,
                "review_summary": review_summary,
            },
            "overall_evaluation": overall_evaluation,
        }

        existing_data.append(data_to_save)

        # Save the updated data to the file
        with open("data/art_writing_data.json", "w") as json_file:
            json.dump(existing_data, json_file, indent=4)

        # Save Art Writing content to file
        if art_writing_content is not None:
            art_writing_file_path = os.path.join("data", "art_writing_content.txt")
            with open(art_writing_file_path, "wb") as art_writing_file:
                art_writing_file.write(art_writing_content)

        st.success("Data saved to JSON and Art Writing content saved successfully!")
    except Exception as e:
        st.error(f"Error saving data to JSON: {e}")

# Run the Streamlit app
if __name__ == "__main__":
    art_writing_portfolio()