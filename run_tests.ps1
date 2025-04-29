$files = @(
    "tests/test_wiki_tool.py",
    "tests/test_web_tool.py",
    "tests/test_news_tool.py",
    "tests/test_knowledge_tool.py",
    "tests/test_research_agent.py",
    "tests/test_outline_agent.py",
    "tests/test_writer_agent.py",
    "tests/test_summary_agent.py",
    "tests/test_generate_article.py"
)

foreach ($file in $files) {
    Write-Host "Running $file..." -ForegroundColor Cyan
    pytest $file
}
