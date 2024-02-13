def match(candidate, job)
    begin
      return job['max_salary'] >= candidate['min_salary'] * 0.9
    rescue StandardError => e
      raise "An error occurred: #{e}"
    end
end