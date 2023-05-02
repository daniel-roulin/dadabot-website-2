<script>
	import Button from '$lib/Button.svelte';

	export let data;

	$: base_path = `/api?chapter=${data.chapter}&exercise=${data.exercise}`;
</script>

<svelte:head>
	<title>Exercise {data.exercise} Chapter {data.chapter}</title>
	<meta property="og:title" content="Exercise {data.exercise} Chapter {data.chapter}" />
	<meta name="twitter:title" content="Exercise {data.exercise} Chapter {data.chapter}" />

	<meta name="description" content="Exercise {data.exercise} of chapter {data.chapter}" />
	<meta property="og:description" content="Exercise {data.exercise} of chapter {data.chapter}" />
	<meta name="twitter:description" content="Exercise {data.exercise} of chapter {data.chapter}" />
</svelte:head>

<div class="img-container">
	<img src="/answers/chapter{data.chapter}/exercise{data.exercise}.png" alt="Answer" />
</div>

<Button
	text="See chapter {data.chapter} pdf"
	on:click={() => {
		window.location.href = '/pdfs/chapter' + data.chapter + '.pdf';
	}}
/>

<style>
	img {
		width: 100%;
	}
</style>
