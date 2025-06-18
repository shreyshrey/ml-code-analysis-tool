import pytest
from pathlib import Path
from test_generator.main import determine_output_path
from test_generator.main import write_test_file
import typer

@pytest.mark.parametrize(
    "source_str, language, expected_str",
    [
        ("src/client.py", "Python", "example_files/test_client.py"),
        ("src/Main.java", "Java", "example_files/MainTest.java"),
        ("scripts/helper.js", "JavaScript", "example_files/helper.test.js"),
    ]
)
def test_determine_output_path(source_str, language, expected_str):
    source_file = Path(source_str)
    expected = Path(expected_str)

    result = determine_output_path(source_file, language)

    assert result == expected


def test_write_test_file_aborts_if_file_exists_and_not_forced(mocker):
    mock_path = mocker.MagicMock(spec=Path)
    
    #Configure its exists() method to return True, simulating that the file exists.
    mock_path.exists.return_value = True
    
    with pytest.raises(typer.Exit) as exc_info:
        write_test_file(mock_path, "some generated code", force=False)
    assert exc_info.value.exit_code == 1
    mock_path.write_text.assert_not_called()