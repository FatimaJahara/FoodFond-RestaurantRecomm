# Restaurant-Recommendation-System-using-collaborative filtering-in-Django-Rest-Framework
## A website to recommend restaurants based on user preference
### GUI (Graphical User Interface)

The GUI for our recommendation Web Application consists of the following items:

#### For Viewers

- Homepage
- About Page
- Login

![Login](https://user-images.githubusercontent.com/54397552/187203392-83c2761b-df64-4f39-bee6-ca1b7b3cc35d.PNG)

- Register

![register](https://user-images.githubusercontent.com/54397552/187203449-fa45a479-5df6-4ac2-8393-52474414c0a8.PNG)


#### For Users(after Logging in)

- Homepage

![HomeLogin](https://user-images.githubusercontent.com/54397552/187203195-0d61653d-5788-4eff-8e4c-2d9a1078d710.PNG)

- About Page

![AboutLogin](https://user-images.githubusercontent.com/54397552/187203347-2e3c9ec0-bbc8-4aad-9807-017e5d277dc1.PNG)

- Search for Restaurants

![Search](https://user-images.githubusercontent.com/54397552/187204355-8bfc93a6-a1b6-4982-a62e-20b1cc5c390e.PNG)

- Recommendation

![Recommend](https://user-images.githubusercontent.com/54397552/187204405-83554d7d-8fe0-4079-9bae-bb0ee4b7d59d.PNG)

- Profile

![Profile](https://user-images.githubusercontent.com/54397552/187204438-d1a06c65-6119-4358-91a8-3142c5f682df.PNG)

- Logout

![Logout](https://user-images.githubusercontent.com/54397552/187204611-03ee7647-2501-4ad1-a66b-344932853f13.PNG)

- Feedback (ongoing..)

![Feedback](https://user-images.githubusercontent.com/54397552/187205152-6c3c902e-fd1a-4cd3-8c29-9035accdd8dd.PNG)

#### For Admins

- Admin Panel

![Admin](https://user-images.githubusercontent.com/54397552/187204539-048c8138-8689-468c-b59d-81b309029f04.PNG)

- Admin Login

![Admin_login](https://user-images.githubusercontent.com/54397552/187204884-7a45bfa8-b8ce-4fd1-b0c2-a2ec5ee06c89.PNG)

- Update recommends
- View Site

### Requirement Specifications

#### Use case text description for users
Use case: Login

Primary actor: Users looking for restaurant recommendations

Goal in context: To login to the account to perform desired task

Preconditions: System must have the ability to store username and password

Trigger: The user decides to click on the login option and used name and password.

Scenerio:
- Users enters the system.
- Clicks login option if not logged in.
- Users can spicify preference
- Users can read review and ratings
- Users can view recommendation

Priority: Essential, must be implemented

When available: First increment

Frequency of use: Many times per day

Channel to actor: Via graphical user interface

Secondary actors: Software engineers

Channel to secondary actors: Codes written

Open issues:
• Is login required for visitors?
• Should there be any way to access the recommendation system without logging in?


![UseCase](https://user-images.githubusercontent.com/54397552/187206259-1bda9c7b-1bde-4a68-8295-93d7a1475cde.png)


#### Activity Diagram

![Activity darker](https://user-images.githubusercontent.com/54397552/187207285-66d07ea3-9317-4fc1-860c-5f0c6b6fa2f7.png)

#### Class Diagram

![ClassDiagram](https://user-images.githubusercontent.com/54397552/187207555-5eb809e6-145f-45b4-a672-6fc79cdaa063.png)

#### Sequence Diagram

![Sequence diagram Restaurant Recommendation System](https://user-images.githubusercontent.com/54397552/187207600-97934cb7-fde7-42f7-982b-14546aa2709a.png)


## Manual Testing

### Requirements/specifications-based system level test cases

- Requirements

![Requirements](https://user-images.githubusercontent.com/54397552/187208363-4198f4ba-43c7-4e69-adb5-381b09fe911c.PNG)

- Login Test Cases

![LoginTestCase](https://user-images.githubusercontent.com/54397552/187208473-ecea8b5d-6834-4412-ac8c-b5262421bec2.PNG)

- Register Test Cases

![RegisterTestCase](https://user-images.githubusercontent.com/54397552/187208901-12769221-ab79-46e7-84d7-ae7c20a0bcc2.PNG)

- Search for Restaurants Test Cases

![UserPreferenceTEst](https://user-images.githubusercontent.com/54397552/187209045-0065b60f-b0fd-4838-abad-b51ae16848c1.PNG)

- Provide Feedback Test Cases

![FeedbackTest](https://user-images.githubusercontent.com/54397552/187209141-c4aab708-3554-4d9b-beaa-ab439889c5eb.PNG)

- Profile Test Cases

![ProfileTest](https://user-images.githubusercontent.com/54397552/187209195-406b34a1-a168-48b5-a93a-95a5135b37b0.PNG)


## Traceability of test cases to use cases

![Traceability](https://user-images.githubusercontent.com/54397552/187209477-42cecbdc-2989-4b16-9b95-d77b348d8876.PNG)
