<template>
    <div>

    <h1 class="centre">Welcome to Flas(h/k) Cards</h1>
    <br>
    <h2 class="centre">You can use this app for learning a new language!!!</h2>
    <h2 class="centre">Login and create multiple decks for different languages</h2>
    <h2 class="centre">Then create multiple cards for different decks</h2>
    <h2 class="centre">Also review and track your progress</h2>
    <br>
    <h2 class="centre">Go to register page for being a registered user. 
        <router-link class="nav-link" to= "/register" >Click Here to register</router-link>
    </h2>
    </div>
</template>

<script>
export default {
    name: 'HomePage'
}
</script>

<style scoped>
.centre{
    text-align: center;
}
</style>