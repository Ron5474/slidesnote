from unittest.mock import patch, MagicMock
from slidenotes.generator import generate

SAMPLE_TEXT = "--- Page 1 ---\nIntroduction to Transformers\nAttention is all you need"

def test_generate_returns_string():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "# Lecture Notes\n## Key Concepts\n- Transformers"

    with patch("slidenotes.generator.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        result = generate(SAMPLE_TEXT)

    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_calls_correct_model():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "# Notes"

    with patch("slidenotes.generator.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        generate(SAMPLE_TEXT)

    call_kwargs = mock_client.chat.completions.create.call_args.kwargs
    assert call_kwargs["model"] == "main"


def test_generate_includes_slide_text_in_prompt():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "# Notes"

    with patch("slidenotes.generator.client") as mock_client:
        mock_client.chat.completions.create.return_value = mock_response
        generate(SAMPLE_TEXT)

    messages = mock_client.chat.completions.create.call_args.kwargs["messages"]
    user_message = next(m for m in messages if m["role"] == "user")
    assert "Transformers" in user_message["content"]
