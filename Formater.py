

def format_time(duration):

  if duration < 60:
    unit = "seconds"
  elif duration < 3600:
    duration /= 60  # Convert to minutes
    unit = "minutes"
  else:
    duration /= 3600  # Convert to hours
    unit = "hours"

  formatted_time = f"{duration:.2f}"

  return f"{formatted_time} {unit}"
