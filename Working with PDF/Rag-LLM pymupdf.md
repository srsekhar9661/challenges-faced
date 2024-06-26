https://artifex.com/blog/creating-a-rag-chatbot-with-chatgpt-and-pymupdf?_gl=1*u7zcf5*_ga*ODEwOTEyNDU0LjE3MTg4MjcxNjI.*_ga_JZTN4VTL9M*MTcxOTA3Nzc0Ni40LjEuMTcxOTA3ODMwNi42MC4wLjA.

# creating the smple bot using pymupddf and chatgpt

## Artifex

Creating a RAG Chatbot with ChatGPT and PyMuPDF
BY HARALD LIEDER - TUESDAY, MARCH 26, 2024
Introduction
Combining Retrieval-Augmented Generation (RAG) technology, ChatGPT's cutting-edge API and PyMuPDF's efficient PDF manipulation capabilities offers a new frontier for creating intelligent chatbots.

These chatbots can tap into vast reserves of knowledge stored in PDF documents, providing responses that are not only contextually aware but also rich in information and insight.

This tutorial will guide you through creating a RAG chatbot that leverages the ChatGPT API for generating responses and PyMuPDF for document processing, highlighting the strengths and simplicity of integrating these powerful tools.

Why Combine ChatGPT API with PyMuPDF?
The ChatGPT API provides access to advanced language models capable of understanding context and generating human-like text. When combined with PyMuPDF, you create a potent mix for a chatbot. This chatbot can consult a wide array of documents to find information relevant to user inquiries, ensuring responses are not only accurate but also highly informative.

Setting Up a Chatbot Using PyMuPDF
Purpose of Our Chatbot
We want to create a chatbot that knows about countries of the world, their capital cities, population sizes and similar information. All we have available as a data basis is a 6-page PDF containing a table with about 200 rows. Each row contains a country name, the name of its national capital, the capital’s population count, its percentage in relation to the country population and the age of this information.

We want to enable the chatbot answering any questions referring to these data – and hopefully also beyond, as far as this geographic and demographic context reaches.

Creating the Chatbot
We will create an application that runs in the command line of a terminal window.

Basis of the following description is an existing example in repository pymupdf/RAG: RAG (Retrieval-Augmented Generation) Chatbot Examples Using PyMuPDF (github.com) where we collect RAG / LLM examples using PyMuPDF. Please look in the folder “country-capitals“ for our example.

There are preliminary steps before we can actually start coding:

OpenAI requests that an application authenticates itself via an API key. Register on OpenAI's website and request an API key for testing purposes if you do not already have one.
 
Edit the source of the script and enter your OpenAI API key.
 
Install or update the following Python packages:
python pip install -U pip
python pip install -U pymupdf
python pip install -U openai
 

Our application will work in “REPL” mode, i.e. in a Read-Evaluate-Process Loop.

When started, it will invoke PyMuPDF once to extract textual information. This text string will be used to build the basis for all subsequent questions from the user.

Like with every chatbot, limitations exist on the size that these text strings may have. These limitations may be different depending on whether the API key is for testing or production purposes etc.

In any case, the function that invokes PyMuPDF for reading the PDF’s content is optimized for small size: it will only read table rows – not the full text of the pages.

See the Python code of the script  - it basically consists of three parts:

Function extract_text_from_pdf(pdf_path).
As mentioned, it will be invoked one time only with the full filename of the PDF. It will return a text string consisting of all table rows, separated by line break characters.
Function generate_response_with_chatgpt(prompt).
This function accesses the chatbot every time after the user has entered a question. The parameter “prompt” is a combination of the actual question with the initial text of the PyMuPDF function.
An endless loop (“while True: …”) that accepts a user question, invokes the chatbot function and outputs the response to the terminal window.
This flowchart shows the interaction between these building blocks:


Using the Chatbot
If all the preparative steps have been successfully executed, our chatbot will show the following behavior.

Whenever the application is ready to accept a question, a “==>” is displayed and anything may be typed in and submitted by hitting ENTER. After a short while, some response is displayed, finished by a line of hyphens  “----------“.

For the sake of clarity, we are coloring the question in red and responses in blue.

$ python country-capitals.py

Loaded 204 table rows from file 'national-capitals.pdf'.

Ready - ask questions or exit with q/Q:

==> what is the capital of Germany?

Response:

The capital of Germany is Berlin.

----------

==> Berlin's population, absolute and relative?

Response:

Berlin's population as of 2021 is 3,677,472. This makes up about 4.4% of the total population of Germany.

----------

The above responses are no surprise because the information is backed by data from the PDF.

The following responses however show that the chatbot indeed has realized the demographic and geographic context and actively searches the internet for additional resources when some question cannot be answered from the PDF data alone.

==> is Vaduz part of the text, and if not, do you know about it?

Response:

No, Vaduz is not part of the text. It is the capital of Liechtenstein.

----------

As our PDF does not include the country Liechtenstein and its capital city Vaduz, the chatbot determined by itself that the word “Vaduz” is a city and the national capital of country Liechtenstein.

Another example: We ask a question that can be answered using PDF data:

==> the 10 smallest capital cities in terms of population?

Response:

1. Vatican City (Vatican City) - 453
2. Ngerulmud (Palau) - 271
3. Adamstown (Pitcairn Islands) - 40
4. Funafuti (Tuvalu) - 6,320
5. Alofi (Niue) - 597
6. Yaren (Nauru) - 747
7. South Tarawa (Kiribati) - 50,182
8. Stanley (Falkland Islands) - 2,460
9. Flying Fish Cove (Christmas Island) - 1,599
10. Roseau (Dominica) - 14,725

----------

However, the following question is interpreted as asking for the 10 smallest cities in terms of their area (square kilometers) – information that must be fully pulled out of internet data:

==> the 10 smallest capital cities of the world?

Response:

1. Vatican City (0.44 km²)
2. Monaco (2.02 km²)
3. Nauru (21 km²)
4. Tuvalu (26 km²)
5. San Marino (61 km²)
6. Liechtenstein (160 km²)
7. Marshall Islands (181 km²)
8. Saint Kitts and Nevis (261 km²)
9. Maldives (298 km²)
10. Malta (316 km²)

----------

Conclusion
By integrating PyMuPDF with a RAG framework, you can build powerful chatbots capable of providing informative and contextually relevant responses. This tutorial only scratches the surface of what's possible. As you become more familiar with PyMuPDF and generative models, you'll find numerous ways to enhance your chatbot's capabilities, making it an invaluable tool for engaging with users and answering their queries effectively.

Remember, the key to a successful RAG chatbot lies in the quality of information it can access. PyMuPDF ensures that extracting this information from PDFs is not only possible but straightforward, showcasing the library's strength and developer-friendliness. Happy coding!

 
## Source Code
See: https://github.com/pymupdf/RAG
Related Blogs 

