import time

def calculate_formatted_process_time(process_function):
  """
  Calculates the execution time of a given process function and returns it in a user-friendly format (seconds, minutes, or hours).

  Args:
      process_function: The function whose execution time needs to be measured.

  Returns:
      A string containing the formatted execution time (e.g., "12.34 seconds").
  """

  start_time = time.time()
  process_function()
  end_time = time.time()

  execution_time = end_time - start_time

  # Determine the appropriate unit (seconds, minutes, or hours)
  if execution_time < 60:
    unit = "seconds"
  elif execution_time < 3600:
    execution_time /= 60  # Convert to minutes
    unit = "minutes"
  else:
    execution_time /= 3600  # Convert to hours
    unit = "hours"

  # Format the output with two decimal places
  formatted_time = f"{execution_time:.2f}"

  return f"{formatted_time} {unit}"

# Example usage
def my_process():
  # Simulate some work that takes time
  for i in range(1000000):
    pass

formatted_time = calculate_formatted_process_time(my_process)
print(f"Process execution time: {formatted_time}")
