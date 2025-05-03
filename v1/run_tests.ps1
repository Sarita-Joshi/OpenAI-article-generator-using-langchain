$files = @(
    "v1/teststest_wiki_tool.py",
    "v1/teststest_web_tool.py",
    "v1/teststest_news_tool.py",
    "v1/teststest_knowledge_tool.py",
    "v1/teststest_research_agent.py",
    "v1/teststest_outline_agent.py",
    "v1/teststest_writer_agent.py",
    "v1/teststest_summary_agent.py",
    "v1/teststest_generate_article.py"
)

foreach ($file in $files) {
    Write-Host "Running $file..." -ForegroundColor Cyan
    pytest $file
}
