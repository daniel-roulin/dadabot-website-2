<script>
    export let search;
    export let placeholder;
</script>

<header>
    <div class="header-items">
        <div class="search">
            <input bind:value={search} on:input type="search" placeholder={placeholder} name="">
            <button on:click={() => {search = ""}} class="button" aria-label="Clear search">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
                    <path fill=#BDBDBD stroke=#BDBDBD d="m12.45 37.65-2.1-2.1L21.9 24 10.35 12.45l2.1-2.1L24 21.9l11.55-11.55 2.1 2.1L26.1 24l11.55 11.55-2.1 2.1L24 26.1Z"/>
                </svg>
            </button>
        </div>
        <a href="/">
            <img class="logo" alt="Dadabot logo" src="/images/logo.webp">
        </a>        
    </div>
    <hr class="divider">
</header>

<style>
header {
    margin: 0;
    padding-top: 10px;
    top: 0px;
    position: sticky;
    background-color: var(--background1);
}

.header-items {
    width: 100%;
    display: flex;
    align-items: center;
}

.logo {
    height: 35px;
    width: 145px;
    margin-left: 15px;
    margin-right: 5px;
}

.divider {
    border: 1px solid var(--secondary2);
}

.search {
    width: 100%;
    height: 35px;
    margin-left: 15px;
    margin-right: 0px;
    border-radius: 50px;
    border: 1px var(--secondary2) solid;
    background-color: var(--background2);

    display: flex;
    align-items: center;
}

.search input[type=search] {
    height: 25px;
    width: 80%;

    font-size: 15px;

    background: none;
    border: none;
    border-color: transparent;
    outline: none;
    color: var(--main);

    padding: 15px;

    flex: 1 1 100px
}

.search,
input::placeholder {
    color: var(--secondary2);
}

.button {
    height: 25px;
    width: 25px;
    padding: 0px;
    margin-right: 10px;
    background: none;
    border: none;
    border-color: transparent;
    flex: 0 1 20px;
}
</style>