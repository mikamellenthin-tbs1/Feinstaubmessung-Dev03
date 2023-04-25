CREATE DATABASE sensordb

CREATE TABLE "sensor" (
	"sensor_id"	INTEGER,
	"sensor_type"	VARCHAR(50),
	"location"	DOUBLE,
	"latiude"	DOUBLE,
	"langitude"	DOUBLE,
	PRIMARY KEY("sensor_id")
);

CREATE TABLE "weather" (
	"id" INTEGER,
	"sensor_id"	INTEGER,
	"timestamp"	DATETIME,
	"humidity"	DOUBLE,
	"temperature"	DOUBLE,
	FOREIGN KEY("sensor_id") REFERENCES sensor_location,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "feinstaub" (
	"id"	INTEGER,
	"sensor_id"	INTEGER,
	"timestamp"	DATETIME,
	"P1"	DOUBLE,
	"dur_P1"	DOUBLE,
	"ratioP1"	DOUBLE,
	"P2"	DOUBLE,
   "dur_P2"	DOUBLE,
   "ratioP2"	DOUBLE,
	FOREIGN KEY("sensor_id") REFERENCES sensor_location,
	PRIMARY KEY("id" AUTOINCREMENT)
);

