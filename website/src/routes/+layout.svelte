<script>
	import Header from '$lib/Header.svelte';
	import Footer from '$lib/Footer.svelte';
	import NavBar from '$lib/NavBar.svelte';
	import Exercises from '$lib/Exercises.svelte';
	import Chapters from '$lib/Chapters.svelte';
	import Subtitle from '$lib/Subtitle.svelte'
	import './styles.css';
	import { queryParam } from "sveltekit-search-params";
	import { page } from '$app/stores';

	$: chapter = $page.data.chapter;

	let search = queryParam("search");
	let result_promise;
	update_search();

	function update_search() {
		let value = $search
		if (value && value.trim().length > 0) {
			result_promise = fetch_search_results(value);
		}
	}

	async function fetch_search_results(value) {
		let url = `/search?q=${value.trim()}`
		if (chapter) {
			url += `&ch=${chapter}`
		}
		let res = await fetch(url);
		return await res.json();
	}
</script>

<div class="app">
	<!-- <Header bind:search={$search} on:input={update_search}/> -->
	<Header placeholder={chapter ? "Search in chapter " + chapter + "..." : "Search..."} bind:search={$search} on:input={update_search}/>
	
	{#if $search && $search.trim().length > 0}
		{#await result_promise}
			<Subtitle text="Loading..." />
		{:then results}
			{#if results.chapters.length !== 0 || results.exercises.length !== 0}
				<Chapters search={$search} subtitle="Chapters" chapters={results.chapters} />
				<Exercises search={$search} subtitle="Exercises" exercises={results.exercises} />
			{:else}
				<Subtitle text="No results" />
			{/if}
		{/await}
	{:else}
		<NavBar />
		<slot />
	{/if}

	<div style="height: 30px;"></div>
	<Footer/>
</div>