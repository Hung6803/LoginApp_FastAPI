const admin = [
    {
        path: "/admin",
        component: () => import("../layouts/admin.vue"),
        children: [
            {
                path:"users",
                name: "admin-users",
                component: () => import("../pages/admin/users/index.vue"),
            },
            {
                path:"users/create",
                name: "admin-users-create",
                component: () => import("../pages/admin/users/create.vue"),
            },
            {
                path:"users/:id/edit",
                name: "admin-users-edit",
                component: () => import("../pages/admin/users/edit.vue"),
            }
        ]
    }
]

export default admin;