<script>
    export let text;
</script>

<button on:click >{text}</button>

<style>
button {
  background-color: var(-secondary2);
  border-radius: 5px;
  border-width: 0;
  color: var(--main);
  cursor: pointer;
  display: inline-block;
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  margin: 10px;
  padding: 10px 12px;
  text-align: center;
  transition: 200ms;
  vertical-align: baseline;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}
</style>