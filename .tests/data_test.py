import os
import subprocess
import pytest

def test_python_script_runs():
    """Test if the Python script executes without errors"""
    
    # Run the Python script using subprocess
    try:
        result = subprocess.run(['python3', 'main.py'], check=True, capture_output=True)
        assert result.returncode == 0, f"Error: {result.stderr.decode()}"
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Error executing main.py: {e.stderr.decode()}")

def test_analysis_content():
    """Ensure the analysis text file contains meaningful content"""
    
    # Check if analysis.txt file exists and contains expected content
    if os.path.exists('analysis.txt'):
        with open('analysis.txt', 'r') as file:
            content = file.read()
            assert len(content) > 0, "Error: analysis.txt is empty."
            assert "correlation" in content.lower(), "Error: analysis.txt does not mention correlation."
    else:
        pytest.fail("Error: analysis.txt is missing.")
