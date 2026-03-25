import re

class PlutoParser:
    KEYWORDS = ["PROCEDURE", "STEP", "MAIN", "END", "WAIT UNTIL", "INITIATE", "CONFIRM", "SET VALUE"]

    @staticmethod
    def format_pluto(code: str) -> str:
        lines = code.split('\n')
        formatted = []
        indent = 0
        for line in lines:
            stripped = line.strip()
            if not stripped: continue
            
            # Enforce Uppercase for Keywords
            for kw in PlutoParser.KEYWORDS:
                stripped = re.sub(f"(?i){kw}", kw, stripped)
            
            # Simple Indentation Logic
            if any(x in stripped for x in ["END", "ELSE"]): indent -= 1
            formatted.append("  " * max(0, indent) + stripped)
            if any(x in stripped for x in ["PROCEDURE", "STEP", "MAIN", "IF"]): indent += 1
            
        return "\n".join(formatted)

    @staticmethod
    def lint_pluto(code: str):
        errors = []
        # Structural Checks
        if "PROCEDURE" in code and "END PROCEDURE" not in code:
            errors.append("Validation Error: Procedure started but never closed with 'END PROCEDURE'")
        if "STEP" in code and ":" not in code:
            errors.append("Syntax Error: Steps require a colon (e.g., STEP 1: Description)")
        
        return {"is_valid": len(errors) == 0, "errors": errors}