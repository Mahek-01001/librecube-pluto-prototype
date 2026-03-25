; -- PLUTO Tree-sitter Highlights --

(procedure_declaration "PROCEDURE" @keyword)
(procedure_declaration "END" @keyword)

[
  "STEP"
  "MAIN"
  "PRECONDITIONS"
  "WATCHDOG"
  "CONFIRMATION"
] @type

[
  "INITIATE"
  "CONFIRM"
  "WAIT"
  "SET"
  "GET"
] @function.builtin

[
  "IF"
  "THEN"
  "ELSE"
  "WHILE"
  "UNTIL"
] @keyword.control

(comment) @comment
(string) @string
(number) @number