# # wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10q/uber_10q_march_2022.pdf' -O './data/uber_10q_march_2022.pdf'
# # wget "https://meetings.wmo.int/Cg-19/PublishingImages/SitePages/FINAC-43/7%20-%20EC-77-Doc%205%20Financial%20Statements%20for%202022%20(FINAC).pptx" -O './data/presentation.pptx'
# import os
# import nest_asyncio  # noqa: E402
# nest_asyncio.apply()

# # bring in our LLAMA_CLOUD_API_KEY
# from dotenv import load_dotenv
# load_dotenv()

# ##### LLAMAPARSE #####
# from llama_parse import LlamaParse

# llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")


# #llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data("./data/presentation.pptx")
# #llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data("./data/uber_10q_march_2022.pdf")
# #llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data("./data/state_of_union.txt")

# import pickle
# # Define a function to load parsed data if available, or parse if not
# def load_or_parse_data():
#     data_file = "./data/parsed_data.pkl"
    
#     if os.path.exists(data_file):
#         # Load the parsed data from the file
#         with open(data_file, "rb") as f:
#             parsed_data = pickle.load(f)
#     else:
#         # Perform the parsing step and store the result in llama_parse_documents
#         #llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data("./data/uber_10q_march_2022.pdf")
#         #llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data("./data/presentation.pptx")
#         llama_parse_documents = LlamaParse(api_key=llamaparse_api_key, result_type="markdown").load_data(["./data/presentation.pptx", "./data/uber_10q_march_2022.pdf"])

#         # Save the parsed data to a file
#         with open(data_file, "wb") as f:
#             pickle.dump(llama_parse_documents, f)
        
#         # Set the parsed data to the variable
#         parsed_data = llama_parse_documents
    
#     return parsed_data

# # Call the function to either load or parse the data
# llama_parse_documents = load_or_parse_data()


# len(llama_parse_documents)

# llama_parse_documents[0].text[:100]

# type(llama_parse_documents)

# ######## QDRANT ###########

# from llama_index.vector_stores.qdrant import QdrantVectorStore
# from llama_index.core import VectorStoreIndex, StorageContext

# import qdrant_client

# qdrant_url = os.getenv("QDRANT_URL")
# qdrant_api_key = os.getenv("QDRANT_API_KEY")

# ######### FastEmbedEmbeddings #############

# # by default llamaindex uses OpenAI models
# from llama_index.embeddings.fastembed import FastEmbedEmbedding
# embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")

# """ embed_model = OllamaEmbedding(
#     model_name="nomic-embed-text",
#     #model_name="llama2",
#     base_url="http://localhost:11434",
#     ollama_additional_kwargs={"mirostat": 0},
# ) """

# #### Setting embed_model other than openAI ( by default used openAI's model)
# from llama_index.core import Settings

# Settings.embed_model = embed_model

# ######### Groq API ###########

# from llama_index.llms.groq import Groq
# groq_api_key = os.getenv("GROQ_API_KEY")

# llm = Groq(model="mixtral-8x7b-32768", api_key=groq_api_key)
# Settings.llm = llm

# client = qdrant_client.QdrantClient(api_key=qdrant_api_key, url=qdrant_url,)

# vector_store = QdrantVectorStore(client=client, collection_name='qdrant_rag')
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(documents=llama_parse_documents, storage_context=storage_context, show_progress=True)
# query_engine = index.as_query_engine()
# query = "what is the letter of credit As of December 31, 2021 "
# response = query_engine.query(query)
# print(response)

import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors

def create_pdf(output_filename="College_FAQ.pdf"):
    # Create PDF document
    doc = SimpleDocTemplate(output_filename, pagesize=A4)
    story = []

    # Define styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading1'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6
    )
    
    subheading_style = ParagraphStyle(
        'Subheading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=6,
        spaceAfter=3
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=10,
        spaceBefore=2,
        spaceAfter=8
    )
    
    # Add title
    story.append(Paragraph("College Frequently Asked Questions", title_style))
    story.append(Spacer(1, 20))

    # Section 1: Admissions
    story.append(Paragraph("Admissions", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. What is the admission process for undergraduate/postgraduate courses?", subheading_style))
    story.append(Paragraph("The admission process typically involves filling out an online/offline application form, submitting required documents, and completing an entrance exam or interview if applicable.", normal_style))
    
    # Q2
    story.append(Paragraph("2. What are the eligibility criteria for specific programs?", subheading_style))
    story.append(Paragraph("Eligibility criteria vary by course and program. For undergraduate courses, a minimum percentage in high school exams is required. For postgraduate courses, a bachelor's degree in the relevant field is mandatory.", normal_style))
    
    # Q3
    story.append(Paragraph("3. How can I apply for admission?", subheading_style))
    story.append(Paragraph("You can apply through the college's official website or visit the admissions office to submit your application.", normal_style))
    
    # Q4
    story.append(Paragraph("4. What is the application deadline?", subheading_style))
    story.append(Paragraph("The deadline depends on the course and admission cycle. Visit the college website or contact the admissions office for specific dates.", normal_style))
    
    # Q5
    story.append(Paragraph("5. What documents are required for admission?", subheading_style))
    story.append(Paragraph("Commonly required documents include:", normal_style))
    story.append(Paragraph("• Mark sheets and certificates (10th, 12th, or graduation)", normal_style))
    story.append(Paragraph("• Passport-sized photographs", normal_style))
    story.append(Paragraph("• Identity proof (Aadhaar, passport, etc.)", normal_style))
    story.append(Paragraph("• Caste certificate (if applicable)", normal_style))
    story.append(Paragraph("• Entrance exam scorecard", normal_style))
    
    # Q6
    story.append(Paragraph("6. Is there an entrance exam? If yes, when and how can I register?", subheading_style))
    story.append(Paragraph("Yes, entrance exams are required for certain courses. Registration details are announced on the college's website, and you must register within the given time frame.", normal_style))
    
    # Q7
    story.append(Paragraph("7. Can I apply for multiple courses at the same time?", subheading_style))
    story.append(Paragraph("Yes, you can apply for multiple courses if they do not have overlapping schedules. Separate applications may be required.", normal_style))
    
    # Q8
    story.append(Paragraph("8. What is the fee structure for various courses?", subheading_style))
    story.append(Paragraph("The fee structure varies by course and program. Refer to the college website or contact the accounts department for detailed information.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 2: Fees and Payments
    story.append(Paragraph("Fees and Payments", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. What are the payment methods for tuition fees?", subheading_style))
    story.append(Paragraph("Payment can be made through online banking, credit/debit cards, UPI, demand drafts, or at the accounts office in cash.", normal_style))
    
    # Q2
    story.append(Paragraph("2. Can I pay the fees in installments?", subheading_style))
    story.append(Paragraph("Yes, some courses allow installment payments. Check with the accounts department for eligibility and payment plans.", normal_style))
    
    # Q3
    story.append(Paragraph("3. What is the late fee policy for delayed payments?", subheading_style))
    story.append(Paragraph("A late fee may be charged for payments beyond the due date. The exact penalty depends on college policy.", normal_style))
    
    # Q4
    story.append(Paragraph("4. How do I apply for a fee refund?", subheading_style))
    story.append(Paragraph("Submit a written application to the accounts office along with proof of payment and reason for refund. Refunds are processed as per the refund policy.", normal_style))
    
    # Q5
    story.append(Paragraph("5. Are there any scholarships or financial aid options available?", subheading_style))
    story.append(Paragraph("Yes, merit-based and need-based scholarships are available. Contact the scholarships office for details and application procedures.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 3: Examinations and Results
    story.append(PageBreak())
    story.append(Paragraph("Examinations and Results", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. When will the exam timetable be released?", subheading_style))
    story.append(Paragraph("The timetable is usually released a month before exams on the college notice board and website.", normal_style))
    
    # Q2
    story.append(Paragraph("2. How can I download my admit card?", subheading_style))
    story.append(Paragraph("Admit cards can be downloaded from the student portal using your login credentials.", normal_style))
    
    # Q3
    story.append(Paragraph("3. Where can I check my results?", subheading_style))
    story.append(Paragraph("Results are published on the official college website and notice boards.", normal_style))
    
    # Q4
    story.append(Paragraph("4. What is the procedure for revaluation/rechecking of exam papers?", subheading_style))
    story.append(Paragraph("Submit a revaluation application form along with the prescribed fee within the stipulated time frame.", normal_style))
    
    # Q5
    story.append(Paragraph("5. How can I obtain a duplicate mark sheet or degree certificate?", subheading_style))
    story.append(Paragraph("Visit the registrar's office with an application form and required ID proof. A nominal fee may apply.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 4: Student Services
    story.append(Paragraph("Student Services", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. How do I apply for a hostel or accommodation?", subheading_style))
    story.append(Paragraph("Fill out the hostel application form during admission or at the hostel office. Allocation is based on availability.", normal_style))
    
    # Q2
    story.append(Paragraph("2. What is the process to get a student ID card?", subheading_style))
    story.append(Paragraph("Submit your photograph and student registration number at the student services office.", normal_style))
    
    # Q3
    story.append(Paragraph("3. How do I access the library or online resources?", subheading_style))
    story.append(Paragraph("Use your student ID card for physical library access. Online resources require a login provided by the library.", normal_style))
    
    # Q4
    story.append(Paragraph("4. Who can I contact for counseling services?", subheading_style))
    story.append(Paragraph("The counseling office is available for academic, career, and personal guidance. Contact details are provided on the college website.", normal_style))
    
    # Q5
    story.append(Paragraph("5. How can I update my contact information in college records?", subheading_style))
    story.append(Paragraph("Submit a written request to the administration office or update it through the student portal.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 5: Academic Queries
    story.append(PageBreak())
    story.append(Paragraph("Academic Queries", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. Where can I find the academic calendar?", subheading_style))
    story.append(Paragraph("The academic calendar is available on the college website and notice boards.", normal_style))
    
    # Q2
    story.append(Paragraph("2. How can I change my course or program?", subheading_style))
    story.append(Paragraph("Submit a formal request to the academic office. Approval depends on seat availability and eligibility.", normal_style))
    
    # Q3
    story.append(Paragraph("3. What is the process for withdrawing from a course?", subheading_style))
    story.append(Paragraph("Fill out the withdrawal form, submit it to the academic office, and clear any pending dues.", normal_style))
    
    # Q4
    story.append(Paragraph("4. How can I get my transcripts or recommendation letters?", subheading_style))
    story.append(Paragraph("Request transcripts or letters from the registrar's office. Processing may take a few days.", normal_style))
    
    # Q5
    story.append(Paragraph("5. Who is my academic advisor, and how can I contact them?", subheading_style))
    story.append(Paragraph("Advisors are assigned during orientation. Contact details are available on the college portal.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 6: Campus Facilities
    story.append(Paragraph("Campus Facilities", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. What are the campus working hours?", subheading_style))
    story.append(Paragraph("The campus operates from 8:00 AM to 6:00 PM, Monday to Saturday.", normal_style))
    
    # Q2
    story.append(Paragraph("2. How can I book facilities like auditoriums or labs for events?", subheading_style))
    story.append(Paragraph("Submit a booking request to the facilities management office.", normal_style))
    
    # Q3
    story.append(Paragraph("3. How can I access sports or gym facilities?", subheading_style))
    story.append(Paragraph("Register at the sports office to obtain access passes.", normal_style))
    
    # Q4
    story.append(Paragraph("4. Where can I report maintenance issues?", subheading_style))
    story.append(Paragraph("Maintenance issues can be reported through the helpdesk or maintenance portal.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 7: Placements and Internships
    story.append(PageBreak())
    story.append(Paragraph("Placements and Internships", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. How can I register for placement drives?", subheading_style))
    story.append(Paragraph("Register through the placement office or the college's placement portal.", normal_style))
    
    # Q2
    story.append(Paragraph("2. What is the placement success rate for my course?", subheading_style))
    story.append(Paragraph("Placement statistics are available on the college website or through the placement office.", normal_style))
    
    # Q3
    story.append(Paragraph("3. Are internships mandatory, and how can I find them?", subheading_style))
    story.append(Paragraph("Internships may be mandatory for some courses. The placement cell or faculty advisors can guide you in finding internships.", normal_style))
    
    # Q4
    story.append(Paragraph("4. Who can I contact for career guidance?", subheading_style))
    story.append(Paragraph("Career guidance is provided by the counseling office or placement cell.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 8: General
    story.append(Paragraph("General", heading_style))
    story.append(Spacer(1, 10))
    
    # Q1
    story.append(Paragraph("1. Where is the college located, and how can I reach it?", subheading_style))
    story.append(Paragraph("The college is located at [address]. Directions and maps are available on the website.", normal_style))
    
    # Q2
    story.append(Paragraph("2. What are the office hours for administrative departments?", subheading_style))
    story.append(Paragraph("Office hours are 9:00 AM to 5:00 PM, Monday to Friday.", normal_style))
    
    # Q3
    story.append(Paragraph("3. How can I get a bonafide or no-objection certificate?", subheading_style))
    story.append(Paragraph("Submit a request at the administration office along with your student ID.", normal_style))
    
    # Q4
    story.append(Paragraph("4. What is the procedure for leaving or transferring to another institution?", subheading_style))
    story.append(Paragraph("Submit a transfer application along with clearance certificates from all departments.", normal_style))
    
    # Q5
    story.append(Paragraph("5. How can I file a complaint or provide feedback?", subheading_style))
    story.append(Paragraph("Use the feedback form available on the website or contact the grievance cell.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Section 9: Events
    story.append(PageBreak())
    story.append(Paragraph("Events", heading_style))
    story.append(Spacer(1, 10))
    
    # Subsection: General Event Information
    story.append(Paragraph("General Event Information", subheading_style))
    story.append(Spacer(1, 5))
    
    # Q1
    story.append(Paragraph("1. What are the upcoming events in the college?", subheading_style))
    story.append(Paragraph("You can view the list of upcoming events on the college website's events section or on the notice boards.", normal_style))
    
    # Q2
    story.append(Paragraph("2. How can I register for an event?", subheading_style))
    story.append(Paragraph("Visit the event page on the college website or contact the event coordinator for registration details.", normal_style))
    
    # Q3
    story.append(Paragraph("3. Where can I find the event schedule?", subheading_style))
    story.append(Paragraph("The event schedule is posted on the official website, notice boards, or sent via email to all students.", normal_style))
    
    # Q4
    story.append(Paragraph("4. Who can participate in college events?", subheading_style))
    story.append(Paragraph("Participation rules vary by event. Some events are open to all students, while others may have specific eligibility criteria.", normal_style))
    
    # Q5
    story.append(Paragraph("5. Can students from other colleges attend the events?", subheading_style))
    story.append(Paragraph("Some events allow external participation. Check the event details or contact the event organizer.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Subsection: Event Types
    story.append(Paragraph("Event Types", subheading_style))
    story.append(Spacer(1, 5))
    
    # Q6
    story.append(Paragraph("6. What types of events does the college organize?", subheading_style))
    story.append(Paragraph("The college organizes cultural festivals, technical fests, sports meets, seminars, workshops, webinars, alumni meets, and more.", normal_style))
    
    # Q7
    story.append(Paragraph("7. Are there any annual cultural or technical festivals?", subheading_style))
    story.append(Paragraph("Yes, our college hosts annual festivals like [Name of Cultural Fest] and [Name of Technical Fest]. Check the website for dates and themes.", normal_style))
    
    # Q8
    story.append(Paragraph("8. Does the college organize placement fairs or job fairs?", subheading_style))
    story.append(Paragraph("Yes, the college organizes annual placement fairs. Keep an eye on announcements from the placement cell.", normal_style))
    
    # Q9
    story.append(Paragraph("9. Are there any sports tournaments held on campus?", subheading_style))
    story.append(Paragraph("Yes, inter-college and intra-college sports tournaments are held regularly. The sports office provides detailed schedules.", normal_style))
    
    # Q10
    story.append(Paragraph("10. What are some clubs or societies that organize events?", subheading_style))
    story.append(Paragraph("Clubs like the Drama Club, Tech Club, Debate Society, and Dance Club frequently organize events.", normal_style))
    
    story.append(PageBreak())
    
    # Subsection: Event Participation
    story.append(Paragraph("Event Participation", subheading_style))
    story.append(Spacer(1, 5))
    
    # Q11
    story.append(Paragraph("11. How can I volunteer for college events?", subheading_style))
    story.append(Paragraph("Contact the event coordinator or register as a volunteer through the event portal.", normal_style))
    
    # Q12
    story.append(Paragraph("12. Is there a fee to participate in events?", subheading_style))
    story.append(Paragraph("Some events have participation fees, while others are free. Check the event details for specific information.", normal_style))
    
    # Q13
    story.append(Paragraph("13. What should I do if I want to host an event?", subheading_style))
    story.append(Paragraph("Submit a proposal to the student council or the administration for approval.", normal_style))
    
    # Q14
    story.append(Paragraph("14. How are winners of events rewarded?", subheading_style))
    story.append(Paragraph("Winners receive certificates, trophies, or cash prizes, depending on the event.", normal_style))
    
    # Q15
    story.append(Paragraph("15. Can I participate in multiple events happening on the same day?", subheading_style))
    story.append(Paragraph("Yes, if the event schedules do not overlap. Check the timing before registering.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Subsection: Event Logistics
    story.append(Paragraph("Event Logistics", subheading_style))
    story.append(Spacer(1, 5))
    
    # Q16
    story.append(Paragraph("16. Where are the events held on campus?", subheading_style))
    story.append(Paragraph("Events are usually held in the auditorium, seminar hall, sports ground, or designated classrooms. Check the event flyer for details.", normal_style))
    
    # Q17
    story.append(Paragraph("17. What is the dress code for events?", subheading_style))
    story.append(Paragraph("The dress code depends on the event. For formal events, business attire may be required, while casual attire is fine for informal events.", normal_style))
    
    # Q18
    story.append(Paragraph("18. Will transportation be provided for off-campus events?", subheading_style))
    story.append(Paragraph("Yes, transportation is provided for registered participants in off-campus events. Contact the event team for details.", normal_style))
    
    # Q19
    story.append(Paragraph("19. What is the procedure to book a venue for an event?", subheading_style))
    story.append(Paragraph("Submit a venue booking request to the administration office or facilities management.", normal_style))
    
    # Q20
    story.append(Paragraph("20. Are meals or refreshments provided during events?", subheading_style))
    story.append(Paragraph("Some events include refreshments, while others may have paid food stalls. Check the event details for specifics.", normal_style))
    
    story.append(Spacer(1, 10))
    
    # Subsection: Event Feedback and Issues
    story.append(Paragraph("Event Feedback and Issues", subheading_style))
    story.append(Spacer(1, 5))
    
    # Q21
    story.append(Paragraph("21. How can I give feedback on an event?", subheading_style))
    story.append(Paragraph("Feedback forms are shared after the event. You can also email your feedback to the event organizer.", normal_style))
    
    # Q22
    story.append(Paragraph("22. Who do I contact for event-related queries?", subheading_style))
    story.append(Paragraph("The event coordinator's contact information is provided in the event announcement.", normal_style))
    
    # Q23
    story.append(Paragraph("23. What should I do if I face issues during an event?", subheading_style))
    story.append(Paragraph("Report any issues to the event volunteers or organizers immediately for assistance.", normal_style))
    
    # Q24
    story.append(Paragraph("24. How can I stay updated about college events?", subheading_style))
    story.append(Paragraph("Subscribe to the college newsletter, follow the official social media handles, or check the notice board regularly.", normal_style))
    
    # Q25
    story.append(Paragraph("25. Are there any penalties for missing an event after registering?", subheading_style))
    story.append(Paragraph("Missing an event without prior notice may lead to disqualification from future participation, depending on the event policy.", normal_style))
    
    # Build the PDF
    doc.build(story)
    return output_filename

# Call the function to create the PDF
if __name__ == "__main__":
    pdf_file = create_pdf()
    print(f"PDF created successfully: {pdf_file}")