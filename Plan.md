# UCL MSc + Summer 2027 Internship Prep Plan

Starting point: UCL MSc Computer Science begins in September 2026.

Career target: be ready to apply for Summer 2027 software engineering or related technical internships.

This plan optimises for employability, not for learning every area of computer science in order. The main outcome is:

- strong Python
- confident Git, GitHub, and terminal use
- SQL and database basics
- data structures and algorithms for interviews
- one polished portfolio project
- a clear CV, GitHub, and LinkedIn profile

## Strategy

Do not wait until every topic is finished before building projects or preparing applications.

The best sequence is:

1. Build core Python, Git, and terminal skill.
2. Learn SQL and basic data structures.
3. Start one main project around Week 3.
4. Continue algorithms while the project grows.
5. Polish the portfolio and CV before applications become urgent.

## Current Progress

Already started:

- Terminal basics through Missing Semester Lectures 1-4.
- Vim basics.
- Data wrangling with `grep`, `cut`, `sort`, `uniq`, `wc`, `head`, `tail`, `sed`, and `awk`.
- Git add, commit, and push.
- Python FizzBuzz practice in `python-practice/fizz_buzz.py`.

Immediate setup task:

```bash
git config --global user.name "Peidi Li"
git config --global user.email "your-email@example.com"
```

This avoids future commits using an automatic local email such as `peidili@mac.home`.

## Phase 1: Python, Git, And Terminal

Target time: 2 weeks, about 40-55 hours.

Goal: become comfortable writing and running Python without relying on tutorials for every step.

Python focus:

- variables
- strings
- lists
- tuples
- sets
- dictionaries
- loops
- functions
- file handling
- exceptions
- classes and objects
- type hints
- dataclasses
- virtual environments
- `pip`
- basic `pytest`

Git and terminal focus:

- `git status`
- `git add`
- `git commit`
- `git push`
- `git pull`
- `git branch`
- `git switch`
- `git merge`
- `pwd`
- `cd`
- `ls`
- `mkdir`
- `touch`
- `cp`
- `mv`
- `rm`
- `grep`
- `find`
- `cat`
- `head`
- `tail`
- `chmod`

Practice:

- Keep using this repo daily.
- Commit small finished exercises.
- Write one short README for each meaningful folder or project.
- Finish the Missing Semester shell/data-wrangling exercises at a beginner level.

Outcome:

- You can write small Python scripts.
- You can use Git without panic.
- You understand the terminal well enough to run programs, inspect files, and debug simple mistakes.

## Phase 2: SQL And Data Structures

Target time: 2 weeks, about 45-60 hours.

SQL focus:

- `SELECT`
- `FROM`
- `WHERE`
- `JOIN`
- `GROUP BY`
- `ORDER BY`
- `HAVING`
- `INSERT`
- `UPDATE`
- `DELETE`
- primary keys
- foreign keys
- indexes
- normalisation

Data structures focus:

- arrays/lists
- stacks
- queues
- hash maps
- linked lists
- trees
- heaps
- graphs
- Big O

Practice:

- Solve easy LeetCode-style problems for arrays, strings, and hash maps.
- Implement simple versions of stacks, queues, linked lists, and trees in Python.
- Write down the time complexity of each solution.

Outcome:

- You can explain why one solution is faster than another.
- You can use SQL for useful queries.
- You are ready to start building a database-backed project.

## Phase 3: Start The Main Project Early

Start around Week 3. Continue alongside algorithms.

Recommended project: mathematics learning platform.

Why this project:

- It connects naturally to your mathematics background.
- It demonstrates practical software engineering.
- It can grow gradually from simple to impressive.

Core features:

- user accounts
- login/logout
- practice questions
- answer checking
- progress tracking
- database
- dashboard
- tests
- clear README
- screenshots

Possible later feature:

- AI explanation helper for wrong answers.

Suggested stack:

- Python
- FastAPI
- SQLite first, PostgreSQL later
- HTML/CSS
- small amount of JavaScript
- `pytest`
- GitHub

Build order:

1. Command-line prototype for questions and answers.
2. SQLite database for users, questions, attempts, and progress.
3. FastAPI backend.
4. Simple web pages.
5. Tests.
6. README and screenshots.
7. Deployment if time allows.

Outcome:

- One polished project is more valuable than five half-finished repos.

## Phase 4: Algorithms And Interview Patterns

Target time: ongoing from Week 3 onward.

Prioritise:

- arrays
- strings
- hash maps
- binary search
- two pointers
- sliding window
- recursion
- trees
- BFS
- DFS
- heaps
- graphs
- basic dynamic programming

Lower priority:

- spending too long on bubble sort or selection sort
- advanced dynamic programming too early
- tries before the common patterns are solid

Weekly routine:

- 5-8 coding problems per week at first.
- Write a short explanation after each problem.
- Track mistakes and repeat patterns.
- Commit clean solutions to GitHub.

Outcome:

- By the start of the MSc, aim for 50-80 solved problems.
- By internship application season, aim for 150+ well-reviewed problems.

## Phase 5: Software Engineering Basics

Target time: 20-30 hours, mixed into project work.

Learn by applying:

- clean code
- functions with clear responsibility
- classes when useful
- composition over excessive inheritance
- refactoring
- logging
- debugging
- unit tests
- integration tests
- README writing
- useful commit messages

Do not over-focus on memorising every design pattern early.

Outcome:

- Your project looks like software, not just a script.
- Recruiters can understand, run, and trust your code.

## Phase 6: Computer Systems And Networking

Target time: 20-30 hours.

Understand:

- CPU
- RAM
- cache
- processes
- threads
- filesystems
- permissions
- environment variables
- HTTP
- HTTPS
- DNS
- TCP/IP

Practice:

- Use terminal tools to inspect files and processes.
- Run a local web server.
- Explain what happens when a browser sends a request to your FastAPI app.

Outcome:

- UCL systems material feels familiar.
- You can talk about how software actually runs.

## Phase 7: Portfolio And Applications

Start before everything feels ready.

Portfolio checklist:

- GitHub profile is tidy.
- Main project has a strong README.
- README includes setup instructions.
- README includes screenshots.
- Project has tests.
- Commit history is readable.
- CV is one page.
- LinkedIn is updated.
- You can explain the project in 60 seconds.

CV should highlight:

- mathematics degree
- UCL MSc Computer Science
- Python
- SQL
- Git/GitHub
- main project
- algorithms/problem-solving practice

Outcome before UCL starts:

- one polished project
- 50-80 coding problems solved
- solid Python
- basic SQL
- comfortable Git and terminal
- first CV draft
- LinkedIn updated

## Weekly Routine

Minimum effective week:

- 3 Python or project sessions
- 2 algorithm sessions
- 1 GitHub cleanup or README session
- 1 review session

Strong week:

- 5 coding sessions
- 3 algorithm sessions
- 2 project sessions
- 1 systems or SQL session
- 1 portfolio/application session

Daily habit:

```text
code something
run it
commit meaningful progress
write down one thing learned
```

## Eight Week Sprint

Week 1:

- Python review.
- Git basics.
- Terminal practice.
- Finish small scripts.

Week 2:

- Classes, files, exceptions, type hints.
- Basic testing with `pytest`.
- More GitHub practice.

Week 3:

- SQL basics.
- Arrays, strings, hash maps.
- Start the maths learning project.

Week 4:

- FastAPI basics.
- SQLite schema.
- Stacks, queues, linked lists.

Week 5:

- Project login/users or question system.
- Trees and recursion.
- Begin README polish.

Week 6:

- Progress tracking dashboard.
- BFS/DFS.
- More tests.

Week 7:

- Project cleanup.
- Binary search, two pointers, sliding window.
- Draft CV and LinkedIn.

Week 8:

- Portfolio polish.
- Mock interview practice.
- Review weak topics.
- Prepare a list of internship targets.

## What To Avoid

- Do not spend months only watching tutorials.
- Do not create many empty repositories just to have more repos.
- Do not postpone the main project until every theory topic is finished.
- Do not ignore README files and presentation.
- Do not treat algorithms as memorisation only.
- Do not let GitHub become messy with unexplained code dumps.

## Useful Resources

Python:

- Python official tutorial
- CS50P
- Automate the Boring Stuff with Python

Git and terminal:

- Missing Semester
- Pro Git book

SQL:

- SQLBolt
- Mode SQL tutorial
- PostgreSQL tutorial

Algorithms:

- NeetCode roadmap
- LeetCode
- VisuAlgo

Web/app engineering:

- FastAPI tutorial
- MDN Web Docs

Systems:

- Missing Semester
- CS50 systems material
- Operating Systems: Three Easy Pieces

## Success Check

You are on track for Summer 2027 internships if you can:

- build and explain one substantial project
- solve common easy problems quickly
- solve many medium problems with guidance and review
- write SQL joins and grouped queries
- use Git and GitHub fluently
- run and debug Python from the terminal
- explain HTTP request/response basics
- show a clean GitHub profile
- send a focused one-page CV
