-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-11-13 18:07:45.756

-- tables
-- Table: Address
CREATE TABLE "Address" (
    "cep" int  NOT NULL,
    "state" Varchar  NOT NULL,
    "streetName" Varchar  NOT NULL,
    "city" Varchar  NOT NULL,
    CONSTRAINT "Address_pk" PRIMARY KEY ("cep","state")
);

-- Table: Comment
CREATE TABLE "Comment" (
    "id" int  NOT NULL,
    "senderId" int  NOT NULL,
    "isTipCreator" boolean  NOT NULL,
    "dateTime" timestamp  NOT NULL,
    "text" Varchar  NOT NULL,
    "Tip_id" int  NOT NULL,
    CONSTRAINT "Comment_pk" PRIMARY KEY ("id")
);

-- Table: Emotion
CREATE TABLE "Emotion" (
    "id" int  NOT NULL,
    "name" Varchar  NOT NULL,
    CONSTRAINT "Emotion_pk" PRIMARY KEY ("id")
);

-- Table: Emotion_Tip
CREATE TABLE "Emotion_Tip" (
    "Emotion_id" int  NOT NULL,
    "Tip_id" int  NOT NULL,
    CONSTRAINT "Emotion_Tip_pk" PRIMARY KEY ("Emotion_id","Tip_id")
);

-- Table: Person
CREATE TABLE "Person" (
    "id" int  NOT NULL,
    "first_name" Varchar  NOT NULL,
    "email" Varchar  NOT NULL,
    "points" int  NOT NULL,
    "password" Varchar  NOT NULL,
    "professional_id" int  NULL,
    "specializationField" Varchar  NULL,
    "phoneNumber" int  NULL,
    "isAdmin" boolean  NULL,
    CONSTRAINT "Person_pk" PRIMARY KEY ("id")
);

-- Table: Person_Emotion
CREATE TABLE "Person_Emotion" (
    "Person_id" int  NOT NULL,
    "Emotion_id" int  NOT NULL,
    CONSTRAINT "Person_Emotion_pk" PRIMARY KEY ("Person_id","Emotion_id")
);

-- Table: Selects
CREATE TABLE "Selects" (
    "id" int  NOT NULL,
    "Person_id" int  NOT NULL,
    "Tip_id" int  NOT NULL,
    "Task_id" int  NOT NULL,
    "Emotion_id" int  NOT NULL,
    "dateTime" timestamp  NOT NULL,
    "hasHelped" boolean  NOT NULL,
    CONSTRAINT "Selects_pk" PRIMARY KEY ("id")
);

-- Table: Task
CREATE TABLE "Task" (
    "id" int  NOT NULL,
    "description" Text  NOT NULL,
    "dueDate" date  NOT NULL,
    "emotionId" int  NOT NULL,
    "completed" boolean  NOT NULL,
    "Tip_id" int  NOT NULL,
    CONSTRAINT "Task_pk" PRIMARY KEY ("id")
);

-- Table: Tip
CREATE TABLE "Tip" (
    "id" int  NOT NULL,
    "name" Varchar  NOT NULL,
    "description" Text  NOT NULL,
    "points" int  NOT NULL,
    "cep" int  NOT NULL,
    "state" Varchar  NOT NULL,
    "buildingNumber" int  NULL,
    "complement" Varchar  NOT NULL,
    "country" Varchar  NOT NULL,
    "validated" boolean  NOT NULL,
    "tipCreatorId" int  NOT NULL,
    CONSTRAINT "Tip_pk" PRIMARY KEY ("id")
);

-- foreign keys
-- Reference: Comment_Tip (table: Comment)
ALTER TABLE "Comment" ADD CONSTRAINT "Comment_Tip"
    FOREIGN KEY ("Tip_id")
    REFERENCES "Tip" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Emotion_Selects (table: Selects)
ALTER TABLE "Selects" ADD CONSTRAINT "Emotion_Selects"
    FOREIGN KEY ("Emotion_id")
    REFERENCES "Emotion" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Emotion_Tip_Emotion (table: Emotion_Tip)
ALTER TABLE "Emotion_Tip" ADD CONSTRAINT "Emotion_Tip_Emotion"
    FOREIGN KEY ("Emotion_id")
    REFERENCES "Emotion" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Emotion_Tip_Tip (table: Emotion_Tip)
ALTER TABLE "Emotion_Tip" ADD CONSTRAINT "Emotion_Tip_Tip"
    FOREIGN KEY ("Tip_id")
    REFERENCES "Tip" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Person_Emotion_Emotion (table: Person_Emotion)
ALTER TABLE "Person_Emotion" ADD CONSTRAINT "Person_Emotion_Emotion"
    FOREIGN KEY ("Emotion_id")
    REFERENCES "Emotion" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Person_Emotion_Person (table: Person_Emotion)
ALTER TABLE "Person_Emotion" ADD CONSTRAINT "Person_Emotion_Person"
    FOREIGN KEY ("Person_id")
    REFERENCES "Person" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Person_association_1 (table: Selects)
ALTER TABLE "Selects" ADD CONSTRAINT "Person_association_1"
    FOREIGN KEY ("Person_id")
    REFERENCES "Person" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Table_10_Tip (table: Tip)
ALTER TABLE "Tip" ADD CONSTRAINT "Table_10_Tip"
    FOREIGN KEY ("state", "cep")
    REFERENCES "Address" ("state", "cep")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Task_Selects (table: Selects)
ALTER TABLE "Selects" ADD CONSTRAINT "Task_Selects"
    FOREIGN KEY ("Task_id")
    REFERENCES "Task" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Task_Tip (table: Task)
ALTER TABLE "Task" ADD CONSTRAINT "Task_Tip"
    FOREIGN KEY ("Tip_id")
    REFERENCES "Tip" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Tip_association_1 (table: Selects)
ALTER TABLE "Selects" ADD CONSTRAINT "Tip_association_1"
    FOREIGN KEY ("Tip_id")
    REFERENCES "Tip" ("id")  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- sequences
-- Sequence: Comment_seq
CREATE SEQUENCE "Comment_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: Emotion_seq
CREATE SEQUENCE "Emotion_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: Person_seq
CREATE SEQUENCE "Person_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: Task_seq
CREATE SEQUENCE "Task_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- Sequence: Tip_seq
CREATE SEQUENCE "Tip_seq"
      INCREMENT BY 1
      NO MINVALUE
      NO MAXVALUE
      START WITH 1
      NO CYCLE
;

-- End of file.

