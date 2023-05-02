<script>
	import { page } from '$app/stores';

    $: path = $page.url ? $page.url.pathname.split("/") : ""
    $: chapter = path[1];
    $: exercise = path[2];
</script>

<h2 class="subtitle-text">
    <a href="/">Chapters</a>
    {#if chapter}
        <em> > </em>
        <a href="/{chapter}">Chapter {chapter}</a>
    {/if}
    {#if exercise}
        <em> > </em>
        <a href="/{chapter}/{exercise}">Exercise {exercise}</a>
    {/if}
</h2>

<style>
h2 {
    /* position: sticky;
    top: 80px; */
    margin: 10px;
    margin-top: 20px;
    margin-bottom: 15px;
    font-weight: 500;
    font-size: 20px;
    /* background-color: var(--background1); */
}
</style>