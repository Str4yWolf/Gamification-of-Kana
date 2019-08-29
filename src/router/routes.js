
const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'Register/', component: () => import('pages/Register.vue') },
      { path: 'Tutorial/', component: () => import('pages/Tutorial.vue') },
      { path: 'Shop/', component: () => import('pages/Shop.vue') },
      { path: 'Settings/', component: () => import('pages/Settings.vue') },
      { path: 'Information/', component: () => import('pages/Information.vue') }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
