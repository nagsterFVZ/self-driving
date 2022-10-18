export default {
    title: 'Self Steering Vehicle',
    description: 'Documentation for the BeCreative self steering car project',
    themeConfig: {
        socialLinks: [
            { icon: 'github', link: 'https://github.com/nagsterFVZ/self-driving' },
          ],
          nav: [
            { text: 'Project', link: '/project/' },
            { text: 'Files', link: '/files/' },
            { text: 'Blogs', link: '/blogs/' },
          ],
        sidebar: {
            '/project/': [
                {
                    text: 'Introduction',
                    items: [
                        { text: 'The Project', link: '/project/' },
                        { text: 'Research', link: '/project/research' },
                        { text: 'Parts', link: '/project/-' },
                    ]
                },
                {
                    text: 'Installation',
                    items: [
                    { text: 'Introduction', link: '/project/-' },
                    { text: 'Research', link: '/project/-' },
                    ]
                },
            ],
            '/files/': [
                {
                    text: 'Vehicle',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
                {
                    text: 'Schematics',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
            ],
            '/blogs/': [
                {
                    text: 'Blogs',
                    items: [
                        { text: 'Floris', link: '/blogs/floris' },
                    ]
                },
            ]
        }
    }
}
  