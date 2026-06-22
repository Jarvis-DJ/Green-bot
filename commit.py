import os
import random
import datetime
import subprocess
import json
import pytz


# 🌿 Inspirational quotes
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is the sum of small efforts, repeated.",
    "Small steps every day.",
    "One more brick in the wall of progress.",
    "Consistency is more important than intensity.",
    "Another line, another win!",
    "Stay curious, keep learning.",
    "Another commit to greatness.",
    "Progress, not perfection.",
    "Just showing up matters.",
    "Every commit counts toward greatness.",
    "Build something you're proud of.",
    "Bit by bit, you create the masterpiece.",
    "The habit of showing up wins the game.",
    "Don’t break the streak — commit today!",
    "From bugs to brilliance — keep coding!",
    "It’s not about perfection. It’s about progress.",
    "You’re one step closer to your goal.",
    "Keep calm and commit on.",
    "Even a tiny push moves the needle."
]


# 🌈 Commit messages
commit_messages = [
    "🚀 Boosting productivity with code magic!",
    "🌈 Painting the contribution graph today",
    "💡 A bright idea strikes again!",
    "🧠 Just thinking in Python",
    "🔥 Staying consistent is key",
    "🤖 One more commit for the bot!",
    "📚 Learning something new today",
    "📝 Daily dose of code",
    "📊 Keeping the graph alive",
    "✨ One step at a time",
    "🎯 Another mark on the roadmap",
    "✅ Small win for the day",
    "📦 Packaging progress, one file at a time",
    "🔧 Tweaked, tuned, and tightened",
    "🧪 Experimented with improvements",
    "🎉 Progress never looked better",
    "💭 Thoughts turned into code",
    "🛠️ Building habits, one commit at a time",
    "📈 Slow and steady climb",
    "🚧 Another brick in the dev wall"
]


# Files to update
target_files = [
    "daily_log.txt",
    "progress.md",
    "inspiration.txt"
]


# ⏰ IST timezone
ist = pytz.timezone("Asia/Kolkata")

now = datetime.datetime.now(ist)

date_key = now.strftime("%Y-%m-%d")

timestamp = now.strftime(
    "%Y-%m-%d %I:%M:%S %p"
)


# Tracker file
counter_file = ".commit_tracker.json"


# Maximum commits per day
MAX_COMMITS = 5



# Load previous data
if os.path.exists(counter_file):

    with open(counter_file, "r") as file:
        data = json.load(file)

else:

    data = {}



# Today's previous commits
today_commits = data.get(
    date_key,
    0
)



# Stop if limit reached
if today_commits >= MAX_COMMITS:

    print(
        "✅ Today's commit limit already reached."
    )

    exit()



# Random commits today
commit_number = random.randint(
    1,
    MAX_COMMITS - today_commits
)



commit_logs = []



# Create commits
for i in range(commit_number):


    quote = random.choice(quotes)

    message = random.choice(commit_messages)

    filename = random.choice(target_files)



    # Update file
    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"\n[{timestamp}] {quote}"
        )



    # Git add
    subprocess.run(
        [
            "git",
            "add",
            filename
        ]
    )



    # Git commit
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            message
        ]
    )



    commit_logs.append(
        f"{timestamp} - {message}"
    )




# Update tracker

data[date_key] = (
    today_commits + commit_number
)



with open(
    counter_file,
    "w"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )




# Save history log

with open(
    "commit_log.txt",
    "a",
    encoding="utf-8"
) as log:


    log.write(
        f"\n[{timestamp}] "
        f"+{commit_number} commits\n"
    )


    for item in commit_logs:

        log.write(
            item + "\n"
        )


    log.write("\n")




print(
    f"✅ {commit_number} commits created successfully!"
)

print(
    f"📅 Date: {timestamp}"
)

print(
    f"📊 Total commits today: "
    f"{today_commits + commit_number}"
)
