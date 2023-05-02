export function getRecentChapters() {
    var recent = localStorage.getItem("recentChapters");
    if (recent) {
        return JSON.parse(recent);
    } else {
        return [];
    }
}

export function setRecentChapter(chapter_data) {
    let recent = getRecentChapters();
    for (var i = 0; i < recent.length; i++) {
        if (recent[i].number == chapter_data.number) {
            recent.splice(i, 1);
            break;
        };
    };
    recent.unshift(chapter_data);
    if (recent.length > 5) {
        recent.pop();
    }
    localStorage.setItem("recentChapters", JSON.stringify(recent));
}

export function getRecentExercises(chapter) {
    var recent = localStorage.getItem(`chapter${chapter}RecentExercises`);
    if (recent) {
        return JSON.parse(recent);
    } else {
        return [];
    }
}

export function setRecentExercise(chapter, exercise_data) {
    let recent = getRecentExercises(chapter);
    for (var i = 0; i < recent.length; i++) {
        if (recent[i].number == exercise_data.number) {
            recent.splice(i, 1);
            break;
        };
    };
    recent.unshift(exercise_data);
    if (recent.length > 10) {
        recent.pop();
    }
    localStorage.setItem(`chapter${chapter}RecentExercises`, JSON.stringify(recent));
}