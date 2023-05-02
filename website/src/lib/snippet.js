

export default function snippet(content, search, limit, crop) {
    if (search.length <= limit) return content;
    const startMarker = "<em>";
    const endMarker = "</em>";
    const pattern = new RegExp(search, "i");
    let finalString = "";
    for (;;) {
        let match = content.search(pattern);
        if (match == -1) {
            break;
        }
        let start = 0
        if (crop && finalString.length == 0 && match > 20) {
            start = content.indexOf(" ", match - 20) + 1;
            finalString = "...";
        }
        finalString += content.slice(start, match)
                    + startMarker
                    + content.slice(match, match + search.length)
                    + endMarker;
        content = content.slice(match + search.length);
    }
    return finalString + content;
}