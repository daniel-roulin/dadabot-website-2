<script>
	import Chapters from "$lib/Chapters.svelte";
	import { onMount } from "svelte";
    import { getRecentChapters } from "$lib/recent.js"

    export let data;

    let all_chapters = data.all_chapters;
    let trending_chapters = data.trending_chapters;
    $: recent_chapters = [];
    onMount(async () => {
        recent_chapters = getRecentChapters();
    });
</script>

<svelte:head>
	<title>Dadabot</title>
    <meta property="og:title" content="Dadabot">
    <meta name="twitter:title" content="Dadabot">
    
	<meta name="description" content="Dadabot: Never do your physics homework again!" />
    <meta property="og:description" content="Dadabot: Never do your physics homework again!">
    <meta name="twitter:description" content="Dadabot: Never do your physics homework again!">
</svelte:head>

<Chapters subtitle="Recent" chapters={recent_chapters} />
<Chapters subtitle="Trending" chapters={trending_chapters} />
<Chapters subtitle="All" chapters={all_chapters} />
