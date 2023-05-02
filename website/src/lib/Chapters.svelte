<script>
	import Subtitle from '$lib/Subtitle.svelte';
	import { setRecentChapter } from '$lib/recent.js';

	import snippet from '$lib/snippet.js';

	export let chapters;
	export let subtitle;
	export let search = null;
</script>

{#if chapters.length !== 0}
	<Subtitle text={subtitle} />
	<div class="chapters-container">
		{#each chapters as chapter}
			<div class="chapter-card">
				<a on:click={() => setRecentChapter(chapter)} href="/{chapter.number}">
					<img src="/thumbnails/chapter{chapter.number}.jpg" alt="{chapter.title} illustration" />
					<div class="chapter-texts-container">
						<h3 class="small-text-bold chapter-small-text-bold">Chapter {chapter.number}</h3>
						{#if search}
							<p class="small-text chapter-small-text">
								{@html snippet(chapter.title, search, 0, false)}
							</p>
						{:else}
							<p class="small-text chapter-small-text">{chapter.title}</p>
						{/if}
					</div>
				</a>
			</div>
		{/each}
	</div>
{/if}

<style>
	.chapter-card {
		box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
		transition: box-shadow 0.3s;
		border-radius: 5px;
		width: 250px;
		margin: 10px;
	}
	@media screen and (max-width: 550px) {
		.chapter-card {
			flex-grow: 1;
		}
	}

	img {
		border-radius: 5px 5px 0 0;
		width: 100%;
		height: 150px;
	}

	.chapter-card:hover {
		box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
	}

	.chapter-texts-container {
		padding: 2px 0px;
	}

	.chapter-small-text-bold {
		margin: 5px;
	}

	.chapter-small-text {
		margin: 5px;
		margin-bottom: 10px;
	}
</style>
