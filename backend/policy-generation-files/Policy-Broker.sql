-- Create your own database using the following template

-- Create users table
CREATE TABLE "users" (
    "user_id" int PRIMARY KEY,
    "name" varchar(50),
    "email" varchar(50) UNIQUE,
    "phone" varchar(15),
    "dob" date,
    "income" int,
    "occupation" varchar(30),
    "theme" bit
);

-- Create insurer_info table
CREATE TABLE "insurer_info" (
    "id" smallint PRIMARY KEY,
    "name" varchar(20),
    "website" varchar(20)
);

-- Create insurance_info table
CREATE TABLE "insurance_info" (
    "insured_id" int,
    "insurer_id" smallint,
    "policy_number" smallint,
    "idv_value" int,
    "risk_factor" smallint,
    "tenure" smallint,
    "purchase_date" date,
    PRIMARY KEY ("insurer_id", "policy_number"),
    FOREIGN KEY ("insurer_id") REFERENCES "insurer_info" ("id"),
    UNIQUE ("insured_id")
);

-- Create policy table
CREATE TABLE "policy" (
    "insurer_id" smallint,
    "vehicle_type" varchar(6),
    "min_idv" int,
    "avg_idv" int,
    "max_idv" int,
    "risk_factor" smallint,
    "tenure" smallint,
    "addons" varchar(4),
    FOREIGN KEY ("insurer_id") REFERENCES "insurer_info" ("id")
);

-- Foreign key linking users to insurance_info via insured_id
ALTER TABLE "insurance_info"
ADD CONSTRAINT "fk_insurance_info_user"
FOREIGN KEY ("insured_id") REFERENCES "users" ("user_id");