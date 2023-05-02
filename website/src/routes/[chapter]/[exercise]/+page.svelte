<script>
    import Button from "$lib/Button.svelte"

    export let data

    $: base_path = `/api?chapter=${data.chapter}&exercise=${data.exercise}`
</script>

<svelte:head>
	<title>Exercise {data.exercise} Chapter {data.chapter}</title>
    <meta property="og:title" content="Exercise {data.exercise} Chapter {data.chapter}">
    <meta name="twitter:title" content="Exercise {data.exercise} Chapter {data.chapter}">
    
	<meta name="description" content="Exercise {data.exercise} of chapter {data.chapter}" />
    <meta property="og:description" content="Exercise {data.exercise} of chapter {data.chapter}">
    <meta name="twitter:description" content="Exercise {data.exercise} of chapter {data.chapter}">
</svelte:head>

<div class="img-container">
    <img src={base_path + "&output_format=img-light"} alt="Answer">
</div>

<Button text="See pdf" on:click={() => {window.location.href = base_path + "&output_format=pdf"}} />

<style>
img {
    width: 100%;
}
</style>