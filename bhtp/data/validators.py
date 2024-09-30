import jsonschema
from jsonschema import validate
from bhtp import messages

# Define the schema
_config_schema = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "username": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "full_name": {"type": "string"}
            },
            "required": ["username", "email", "full_name"]
        },
        "input": {
            "type": "object",
            "properties": {
                "local": {"type": "string"},
                "github": {"type": "string"}
            },
            "required": ["local", "github"]
        },
        "ouput": {
            "type": "object",
            "properties": {
                "local": {"type": "string"},
                "drive": {"type": "string"}
            },
            "required": ["local", "drive"]
        }
    },
    "required": ["user", "input", "ouput"]
}

# Validation function
def validate_config(data):
    try:
        validate(instance=data, schema=_config_schema)
        print("Validation successful!")
    except jsonschema.exceptions.ValidationError as e:
        messages.bad_config_file()
        #(f"Validation error: {e.message}")

def main():
    # Sample data
    data = {
        "user": {
            "username": "PoivronJaune",
            "email": "poivronjaune@gmail.com",
            "full_name": "Robert Boivin"
        },
        "input": {
            "local": "data.csv",
            "github": "some_url"
        },
        "ouput": {
            "local": "results.json",
            "drive": "some_url"
        }
    }

    # Run validation
    validate_config(data)

if __name__ == '__main__':
    main()