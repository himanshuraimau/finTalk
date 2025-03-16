import warnings
# Filter out the specific SyntaxWarnings from pydub
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pydub.utils")

# Rest of your imports and application code
# ...existing code...