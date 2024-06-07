import fitz

def fill_pdf_fields(pdf_path, output_path, field_data):
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        if page_num == 2:
            print(page.get_text())
        # Iterate over the field_data dictionary
        for key, value in field_data.items():
            # Search for the key in the text
            text_instances = page.search_for(key)
            # import pdb;pdb.set_trace()
            print(text_instances)
            
            
            # Replace the key with the corresponding value
            for text_instance in text_instances:
                page.add_redact_annot(text_instance)
                page.apply_redactions()
                page.insert_text(text_instance[:2], value)
    
    pdf_document.save(output_path)
    pdf_document.close()

    print(f"PDF saved to {output_path}")

# Example usage
if __name__ == "__main__":
    pdf_path = "C:/Users/sekhar/Downloads/Fillable-Form_CIOMS-to-E2B.pdf"
    output_path = "C:/Users/sekhar/Downloads/test2.pdf"



    field_data = {
        "SUSPECT ADVERSE REACTION REPORT": "Adverse Reaction Report by raja sekhar",
        "1a": 'INDIA',
    }
    
    fill_pdf_fields(pdf_path, output_path, field_data)
