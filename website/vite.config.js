import { sveltekit } from '@sveltejs/kit/vite';
import { ssp } from "sveltekit-search-params/plugin";

/** @type {import('vite').UserConfig} */
const config = {
	plugins: [ssp(), sveltekit()],
	// build: {
	// 	chunkSizeWarningLimit: 1600,
	//   },
};

export default config;