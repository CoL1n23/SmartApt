CREATE table Resident (Name varchar(20), Career varchar(20), ResidentId varchar(20), PlateNum varchar(20), RoomId varchar(20));
INSERT INTO Resident VALUES ('John Doe','Student','R001', 'ABC001', '001A');
INSERT INTO Resident VALUES ('Jeff Zhu', 'Student', 'R002', 'ABC002', '001B');
INSERT INTO Resident VALUES ('Alec Wilson', 'Employee', 'R003', 'ABC003', '001C');

CREATE table Student (Name varchar(20), SchoolName varchar(20), StudentId varchar(20), GraduationYear INT, ResidentId varchar(20), Major varchar(30));
INSERT INTO Student VALUES ('John Doe','Purdue University','00000-00001', 2020, 'R001', 'Computer Science');
INSERT INTO Student VALUES ('Jeff Zhu', 'Purdue University', '00000-01000', 2021, 'R002', 'Computer Science');
INSERT INTO Student VALUES ('Alec Wilson', 'Purdue University', '00000-10000', 2021, 'R003', 'Computer Science');

CREATE table Employee (EmployeeId varchar(20), CompanyName varchar(30), Job varchar(20), Salary INT, ResidentId varchar(20), EducationStatus varchar(20));
INSERT INTO Employee VALUES ('Alec Wilson', 'Purdue University', 'Research Assistant', '100000', 'R003', 'B.S.');
