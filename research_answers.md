# Research

## Python Requests, JSON, XML and RESTful APIs

### 1. Python Requests Module

The Python `requests` module is a library used to send HTTP requests to web servers and APIs. It allows Python applications to communicate with other systems and exchange information over the internet. The module supports common HTTP methods such as GET, POST, PUT and DELETE. GET retrieves information, POST sends new information, PUT updates existing information, and DELETE removes information.

The response returned by a server contains details such as a status code, headers and response data. The `requests` module can also process JSON responses using the `.json()` method. Developers should use timeouts and error handling to manage connection problems and unsuccessful responses.

**Example of using the Requests module:**

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10
)

response.raise_for_status()

data = response.json()

print(data)
```

This example sends a GET request to an API, checks whether the request was successful, converts the JSON response into Python data and displays the result.

### 2. JSON (JavaScript Object Notation)

JSON is a lightweight data format used to store and exchange information between applications. It represents information using key-value pairs and supports data types such as strings, numbers, Boolean values, arrays, objects and null values. JSON is commonly used when web applications communicate with RESTful APIs.

#### Advantages of JSON

- **Easy to read:** Its structure is relatively simple for people to understand.
- **Lightweight:** JSON generally uses less data than more verbose formats, reducing the amount of information transferred.
- **Language support:** Many programming languages can create, read and process JSON.
- **Suitable for APIs:** It is commonly supported by web services and RESTful APIs.
- **Easy to process:** Python can convert JSON data into dictionaries and lists.

#### Disadvantages of JSON

- **Limited data types:** JSON does not directly support specialised data types such as dates, so agreed representations are required.
- **No comments:** The standard JSON format does not support comments.
- **No built-in schema enforcement:** Additional validation is needed to ensure that data follows the required structure.
- **Less suitable for complex document structures:** Nested information can become difficult to manage when the structure is very large.
- **No native binary support:** Binary information normally needs to be encoded before it can be included.

### 3. XML (Extensible Markup Language)

XML is a markup language used to store, describe and exchange structured information. It uses elements enclosed by opening and closing tags. Users can define their own tags to describe the information being stored. XML is often used in systems that require structured documents, configuration files and data exchange between different applications.

#### Advantages of XML

- **Extensible:** Users can define their own tags to represent different types of information.
- **Self-descriptive:** Tags explain the meaning of the information they contain.
- **Supports complex structures:** XML can represent nested data and hierarchical relationships.
- **Validation:** XML Schema and DTD can be used to check whether documents follow defined structures.
- **Platform independent:** Different systems and programming languages can process XML.

#### Disadvantages of XML

- **Verbose:** Opening and closing tags increase the size of documents.
- **More bandwidth:** Larger documents can require more network resources to transfer.
- **Complex processing:** XML parsing and validation can be more complicated than processing simple JSON data.
- **Slower to process in some situations:** Its larger structure can require more processing than lightweight formats.
- **Security risks:** Unsafe XML parser configurations can expose applications to attacks such as XML External Entity (XXE) attacks.

### 4. RESTful APIs

A RESTful API is an application programming interface designed around the principles of Representational State Transfer (REST). It allows different software applications to communicate over HTTP by accessing and manipulating resources. A resource can represent an object such as a product, customer or order. Each resource is normally identified by a URL or URI.

RESTful APIs commonly use HTTP methods. GET retrieves a resource, POST creates a resource, PUT updates a resource, and DELETE removes a resource. Information is often exchanged in JSON format, although other representations can also be used.

REST follows a stateless communication approach, meaning that each request should contain the information needed by the server to process it rather than relying on stored client session context from a previous request.

#### Advantages of RESTful APIs

- **Platform independent:** Applications written in different programming languages can communicate through HTTP.
- **Scalable:** Stateless requests make it easier to distribute requests across multiple servers.
- **Flexible data formats:** REST APIs can support formats such as JSON and XML.
- **Separation of concerns:** The client and server can be developed and maintained separately.
- **Uses standard HTTP methods:** Common operations can be performed using familiar methods such as GET, POST, PUT and DELETE.

#### Disadvantages of RESTful APIs

- **Network dependency:** Applications need a working network connection to communicate with remote services.
- **Multiple requests:** Retrieving related information may require several separate API requests.
- **Security requirements:** Authentication, authorisation, encryption and input validation must be implemented correctly.
- **No fixed standard for every design detail:** Different developers may design REST APIs differently, making integration less consistent.
- **Version management:** Changes to an API can affect existing applications and may require versioning to maintain compatibility.

### Conclusion

Python Requests, JSON, XML and RESTful APIs are important technologies used in application development and communication between software systems. The Requests module allows Python applications to send and receive HTTP requests. JSON and XML provide structured formats for exchanging information, while RESTful APIs define principles for accessing and managing resources over HTTP. Understanding their advantages and disadvantages helps developers select suitable approaches when building reliable and efficient applications.