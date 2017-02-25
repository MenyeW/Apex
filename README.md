# Apex
We have chosen the "Make Commerce Happen" problem. Given the problem statement, we consider the entitites and use cases involved first. We have created a use case flow diagram and defined the various basic use cases that the platform has to handle. On top of that, we brainstormed some features that would help set us apart from the competition and some challenges and pros/cons in making them happen. We then started designing the schema for our database including details such as the tables and their fields, brainstorming on how to best optimize the underlying database for scalability since much of the scalability and manageability of the system is going to come from the database.

We have settled on the following additional features in the project on top of the basic requirements:
- Operation dependent discounts/offers for clients
- Auto up-grade deliveries for consumer (Wow factor)
- Configurable per-transaction or per-client based profit margins
- Priority based internal routing (faster/more cost effective deliveries)
- Multiple priority options for the client for improved delivery speeds / lower costs

Other than these features, we have also brainstormed a few ideas for applying data science and analytics to the data we gather during operation and enable useful insights such as:
- Predictive modeling of hub reliability based on the percentage of successful deliveries as compared to total deliveries routed through the hub
- Modeling and analysis of a hub-level basket analysis to gain insights such as: Is there an item set X that is more in demand around hub Y or not
- Using quotation history data to improve service reception by companies. For example, if a company has been taking quotes but not making final bookings it might mean that they are interested in the service but the pricing model is not attractive. Appropriate steps can be taken to enhance clients' experience and offer incentives to them to choose Careem over the competition
- Above analytics can also be used to determine the success/failure of various priority options and other pricing models that have been offered to clients
