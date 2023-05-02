<script>
    import { onMount } from "svelte";
    import "pdfjs-dist/web/pdf_viewer.css"

    export let pdf_path;

    $: ready = false;
    $: error = null;
    
    onMount(async () => {
        const pdfjsLib = await import('pdfjs-dist/legacy/build/pdf');
        const pdfjsWorker = await import('pdfjs-dist/legacy/build/pdf.worker.entry');
        pdfjsLib.GlobalWorkerOptions.workerSrc = pdfjsWorker;
        
        var canvas = document.getElementById('pdf_renderer');
        var context = canvas.getContext('2d');

        var pdfDoc = null;
        var rendering = false;
        var renderPending = false;

        pdfjsLib.getDocument(pdf_path).promise.then(function(pdfDoc_) {
            pdfDoc = pdfDoc_;
            render();
        }).catch(_error => {
            ready = true;
            error = _error;
        });
        window.addEventListener("resize", render);

        function render() {
            pdfDoc.getPage(1).then(function(page) {
                if (!pdfDoc) return;
                if (rendering) {
                    renderPending = true;
                    return;
                };
                rendering = true;
                
                var viewport = page.getViewport({ scale: 1, });
                // TODO: Set minimum width for mobile
                var scale = document.body.offsetWidth / viewport.width;
                var scaledViewport = page.getViewport({ scale: scale, });

                // Support HiDPI-screens.
                var outputScale = window.devicePixelRatio || 1;

                canvas.width = Math.floor(scaledViewport.width * outputScale);
                canvas.height = Math.floor(scaledViewport.height * outputScale);
                canvas.style.width = Math.floor(scaledViewport.width) + "px";
                canvas.style.height =  Math.floor(scaledViewport.height) + "px";

                var transform = outputScale !== 1
                ? [outputScale, 0, 0, outputScale, 0, 0]
                : null;

                var renderContext = {
                    canvasContext: context,
                    transform: transform,
                    viewport: scaledViewport
                };
                var renderTask = page.render(renderContext);
    
                // Wait for rendering to finish
                renderTask.promise.then(function() {
                    return page.getTextContent();
                }).then(function(textContent) {
    
                    // Assign CSS to the textLayer element
                    var textLayer = document.querySelector(".textLayer");
                    if (!textLayer) return;

                    textLayer.style.left = canvas.offsetLeft + 'px';
                    textLayer.style.top = canvas.offsetTop + 'px';
                    textLayer.style.height = canvas.offsetHeight + 'px';
                    textLayer.style.width = canvas.offsetWidth + 'px';
    
                    // Pass the data to the method for rendering of text over the pdf canvas.
                    pdfjsLib.renderTextLayer({
                        textContent: textContent,
                        container: textLayer,
                        viewport: scaledViewport,
                        textDivs: []
                    }).promise.then(() => {
                        ready = true;
                        error = null;
                        rendering = false;
                        if (renderPending) {
                            renderPending = false;
                            render();
                        }
                    });
                });
            });
        }
    });
</script>

<canvas id="pdf_renderer"></canvas>
<div class="textLayer"></div>
{#if !ready}
    <!-- TODO: Spinner ? -->
    <p>Loading answer...</p>
{/if}
{#if error}
    <p class="highlight-text">{error}</p>
{/if}

<style>
    canvas, .textLayer {
        height: 0;
    }
</style>