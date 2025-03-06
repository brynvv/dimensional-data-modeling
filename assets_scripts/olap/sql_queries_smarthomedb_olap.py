
create_fact_smart_home=('''CREATE TABLE IF NOT EXISTS fact_smart_home (
  id integer,
  energy_use_kwh DECIMAL(18, 2),
  energy_gen_kwh DECIMAL(18, 2),
  furnace1_kwh DECIMAL(18, 2),
  furnace2_kwh DECIMAL(18, 2),
  homeoffice_kwh DECIMAL(18, 2),
  fridge_kwh DECIMAL(18, 2),
  winecellar_kwh DECIMAL(18, 2),
  garagedoor_kwh DECIMAL(18, 2),
  kitchen12_kwh DECIMAL(18, 2),
  kitchen14_kwh DECIMAL(18, 2),
  kitchen38_kwh DECIMAL(18, 2),
  barn_kwh DECIMAL(18, 2),
  well_kwh DECIMAL(18, 2),
  microwave_kwh DECIMAL(18, 2),
  livingroom_kwh DECIMAL(18, 2),
  solar_gen__kwh DECIMAL(18, 2),
  temperature_kwh DECIMAL(18, 2),
  humidity DECIMAL(18, 2),
  visibility DECIMAL(18, 2),
  apparent_temp DECIMAL(18, 2),
  pressure DECIMAL(18, 2),
  windspeed DECIMAL(18, 2),
  windbearing DECIMAL(18, 2),
  precip_intensity DECIMAL(18, 2),
  dewpoint DECIMAL(18, 2),
  precip_probability DECIMAL(18, 2),
  time_id integer,
  weather_id integer,
  cloud_cover_id integer)''') 

create_dim_time=('''CREATE TABLE IF NOT EXISTS dim_time (
  time_id integer,
  timestamp timestamp,
  year integer,
  month integer,
  day integer,
  hour integer,
  minute integer,
  part_of_day varchar(20))''')    

create_dim_weather=('''CREATE TABLE IF NOT EXISTS dim_weather (
      weather_id integer,
      weather_summary VARCHAR(255),
      weather_summary_detailed VARCHAR(255))''')
                       
create_dim_cloud_cover=('''CREATE TABLE IF NOT EXISTS dim_cloud_cover (
      cloud_cover_id integer,
      cloud_cover VARCHAR(255))''')



create_table_queries = [create_fact_smart_home, create_dim_time, create_dim_weather, create_dim_cloud_cover]
