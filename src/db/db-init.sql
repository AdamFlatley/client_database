CREATE TABLE "Contacts" (
  "contact_id" INT NOT NULL,
  "CompanyName" varchar(36) NOT NULL,
  "ContactName" varchar(36),
  "Phone" varchar(36),
  "Extension" varchar(36),
  "Address1" varchar(36),
  "Address2" varchar(36),
  "City" varchar(36),
  "County" varchar(36),
  "Postcode" varchar(36),
  "Email" varchar(36),
  "Website" varchar(36),
  "Other" varchar(36),
  PRIMARY KEY ("contact_id", "CompanyName")
);

CREATE TABLE "Notes" (
  "id" INT PRIMARY KEY NOT NULL,
  "contact_id" INTEGER,
  "The_note" TEXT,
  "note_date" DATE,
  "note_time" TIME
);

CREATE TABLE "Activites" (
  "id" INT PRIMARY KEY NOT NULL,
  "contact_id" INTEGER,
  "The_activity" TEXT,
  "activity_date" DATE,
  "activity_time" TIME
);

CREATE TABLE "Secondary_Contacts" (
  "id" INT PRIMARY KEY NOT NULL,
  "contact_id" INTEGER,
  "The_note" TEXT,
  "note_date" DATE,
  "note_time" TIME
);

ALTER TABLE "Contacts" ADD FOREIGN KEY ("contact_id") REFERENCES "Notes" ("contact_id");

ALTER TABLE "Contacts" ADD FOREIGN KEY ("contact_id") REFERENCES "Secondary_Contacts" ("contact_id");

ALTER TABLE "Contacts" ADD FOREIGN KEY ("contact_id") REFERENCES "Activites" ("contact_id");

