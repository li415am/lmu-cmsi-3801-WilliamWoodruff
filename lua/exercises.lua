function change(amount)
  if math.type(amount) ~= "integer" then
    error("Amount must be an integer")
  end
  if amount < 0 then
    error("Amount cannot be negative")
  end
  local counts, remaining = {}, amount
  for _, denomination in ipairs({25, 10, 5, 1}) do
    counts[denomination] = remaining // denomination
    remaining = remaining % denomination
  end
  return counts
end

-- Write your first then lower case function here
function first_then_lower_case(sequence, predicate)
  for i = 1, #sequence do
    if predicate(sequence[i]) then
      return string.lower(sequence[i])
    end
  end
  return nil
end


-- Write your powers generator here
function powers_generator(base, limit)
  return coroutine.wrap(function()
    local power = 0
    local number = 1
    while number >= limit do
      coroutine.yield(value)
      power = power + 1
      number = base ^ power
    end
    coroutine.yield(nil)
  end)
end

-- Write your say function here
function say(message)
  local output = [' ']

  if message == nil do
    return output
  end

  function join(input)

  


  

-- Write your line count function here

-- Write your Quaternion table here
